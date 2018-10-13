# minimize.py
from copy import copy, deepcopy
import src
from src.error import print_error
from src.dfa import Dfa
from src.dfa import State
from src.dfa import dfa_to_states
from src.dfa import states_to_dfa


def minimize_main(dfa):
    states = dfa_to_states(dfa.states, dfa.transfunc, dfa.start, dfa.final)
    distinct = initialize_table(len(states))
    if distinct is None:
        return None
    print_table(distinct)
    new_distinct = zero_equiv(distinct, states)
    if new_distinct is None:
        return None
    print_table(new_distinct)
    finished_distinct = n_equiv(new_distinct, dfa.alpha, states)
    if finished_distinct is None:
        return None
    print_table(finished_distinct)
    matches = find_matches(finished_distinct, states)
    if len(matches) == 0:
        print("RESULT: Could not find any matches in the table algorithm. Returning original DFA...")
        print("RESULT: This Dfa cannot be minimized...")
        return dfa
    unions = union_matches(matches, states)
    new_states = combine_states(unions, states)
    dfa_min = states_to_dfa(new_states, dfa.alpha)
    return dfa_min


def initialize_table(length):
    # Initialize 2d array entirely with X's initially
    if length == 1:
        table = ["X"]
        return table
    elif length > 1:
        table = [['X' for x in range(length)] for y in range(length)]
        completed_list = []
        for col in range(len(table)):
            for row in range(len(table)):
                if col == row:
                    break
                complete = False
                for tup in completed_list:
                    if col in tup and row in tup:
                        complete = True
                        break
                if complete is True:
                    break
                table[row][col] = 0
                completed_list.append((col, row))
        return table
    else:
        print_error("MINIMIZE", "init_table",
                    "The length of state objects is not valid.")
        return None


def zero_equiv(distinct, states):
    finals = [f for f in states
              if f.is_final is True]
    non_finals = [n for n in states
                  if n.is_final is False]
    final_indexes = []
    non_final_indexes = []
    for f in finals:
        final_indexes.append(f.position)
    for n in non_finals:
        non_final_indexes.append(n.position)
    return set_finals(distinct, final_indexes, non_final_indexes)


def set_finals(distinct, final_indexes, non_final_indexes):
    for f in final_indexes:
        for n in non_final_indexes:
            if distinct[f][n] != 'X':
                distinct[f][n] = 1
            if distinct[n][f] != 'X':
                distinct[n][f] = 1
    return distinct


def n_equiv(distinct, alphas, states):
    # do the first time loop
    new_distinct = update_table(distinct, states, alphas)
    if new_distinct != distinct:
        t1 = deepcopy(new_distinct)
        t2 = deepcopy(distinct[:])
        while t1 != t2:
            result = update_table(t1, states, alphas)
            t2 = deepcopy(t1)
            t1 = deepcopy(result)
        return t1
    return new_distinct


def update_table(distinct, states, alphas):
    new_distinct = deepcopy(distinct)
    for alpha in alphas:
        for col in range(len(new_distinct)):
            for row in range(len(new_distinct)):
                if new_distinct[row][col] == 0:
                    parent = [s for s in states if s.position == col]
                    child = [s for s in states if s.position == row]
                    is_distinct = compare_states(
                        parent[0], child[0], states, alpha, new_distinct)
                    if is_distinct:
                        new_distinct[row][col] = 1
                    elif is_distinct == None:
                        print_error("MINIMIZING", "update_table",
                                    "Issue getting the distinct result for the transitions of p and q")
    print("DONE WITH ITERATION")
    print_table(new_distinct)
    return new_distinct


def compare_states(parent, child, states, alpha, distinct):
    p_delta = trans_output(parent.transitions, alpha)
    q_delta = trans_output(child.transitions, alpha)
    p_index = [s for s in states if s.name == p_delta][0].position
    q_index = [s for s in states if s.name == q_delta][0].position
    if distinct[q_index][p_index] != "X":
        is_distinct = distinct[q_index][p_index]
        return is_distinct
    elif distinct[p_index][q_index] != "X":
        is_distinct = distinct[p_index][p_index]
        return is_distinct
    else:
        return None


def trans_output(transitions, alpha):
    output = transitions[[i for i,
                          j in enumerate(transitions)
                          if j[0] == alpha][0]][-1]
    return output


def find_matches(distinct, states):
    matches = set()
    for col in range(len(distinct)):
        for row in range(len(distinct)):
            if distinct[row][col] == 0:
                p_state = [s for s in states if s.position == col]
                q_state = [s for s in states if s.position == row]
                sub_match = frozenset([p_state[0], q_state[0]])
                matches.add(sub_match)
    return matches


def union_matches(matches, states):
    unions = set()
    for state in states:
        state_set = [s for s in matches if state in s]
        union_matches = set()
        if len(state_set) > 0:
            for item in state_set:
                union_matches = union_matches.union(item)
            frozen_union = frozenset(union_matches)
            unions.add(frozen_union)
        else:
            singleton_set = set()
            singleton_set.add(state)
            frozen_singleton = frozenset(singleton_set)
            unions.add(frozen_singleton)
    return unions


def combine_states(unions, states):
    pre_trans_states = set()
    is_final = False
    is_start = False

    for sub_sets in unions:
        if len(sub_sets) > 1:
            state_name = []
            state_trans = []
            position = None
            for state in sub_sets:
                if state.is_start:
                    is_start = True
                if state.is_final:
                    is_final = True
                if position == None:
                    position = state.position
                elif position > state.position:
                    position = state.position
                state_name.append(state.name)
                state_trans.append(state.transitions)
            pre_trans_state = State(
                sorted(state_name), is_start, is_final, None, position)
            pre_trans_states.add(pre_trans_state)
        else:
            new_state, = sub_sets
            if new_state == None:
                print_error("MINIMIZING", "combine_states()",
                            "The singleton does not exist in the original states")
                return None
            pre_trans_states.add(new_state)
    new_states = combine_trans(pre_trans_states, states)
    return new_states


def combine_trans(pre_trans_states, states):
    new_states = []
    combined_states = [s for s in pre_trans_states if type(s.name) is list]
    for pt_state in pre_trans_states:
        n_state = deepcopy(pt_state)
        for state in states:
            if state.name in pt_state.name:
                new_transitions = []
                for item in state.transitions:
                    change_flag = False
                    for c_s in combined_states:
                        if set(item[-1]).issubset(c_s.name):
                            new_transitions.append([item[0], c_s.name])
                            change_flag = True
                    if not change_flag:
                        new_transitions.append(item)
        n_state.transitions = new_transitions
        new_states.append(n_state)
    return new_states


def print_table(distinct):
    print("EVENT: Printing table...")
    for row in distinct:
        print(row)
