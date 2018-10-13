# minimize.py
import src
from src.error import print_error
from src.dfa import Dfa
from src.dfa import State
from src.dfa import states_to_dfa


def minimize_main(dfa):
    states = dfa.to_state_objects()
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
    a_index = 0
    new_distinct = update_table(distinct, states, alphas[a_index])
    a_index += 1
    return _helper_equiv(new_distinct, a_index)

    def _helper_equiv(distinct, a_index):
        nonlocal alphas
        nonlocal states
        if a_index is not None:
            print("EVENT: n_equiv(): alpha (index,letter): ("
                  + str(a_index) + "," + alphas[a_index] + ")")
            # do all the other loops
            if a_index < len(alphas):
                new_distinct = update_table(distinct, states, alphas[a_index])
                a_index += 1
                print_table(new_distinct)
                _helper_equiv(new_distinct, a_index)
            else:
                _helper_equiv(distinct, None)
        else:
            # Were done here
            return distinct


def update_table(distinct, states, alpha):
    completed_list = []
    for col in range(len(distinct)):
        for row in range(len(distinct)):
            complete = False
            if col == row or distinct[row][col] == 'X':
                break
            if distinct[row][col] == 1:
                completed_list.append((col, row))
                break
            for tup in completed_list:
                if col in tup and row in tup:
                    complete = True
                    break
            if complete is True:
                break
            if distinct[row][col] == 0:
                parent = [s for s in states if s.position == col]
                child = [s for s in states if s.position == row]
                is_distinct = compare_states(
                    parent, child, states, alpha, distinct)
                completed_list.append((col, row))
                if is_distinct:
                    distinct[row][col] = 1
                elif not is_distinct:
                    distinct[row][col] = 0
                else:
                    print_error("MINIMIZING", "update_table",
                                "Issue getting the distinct result for the transitions of p and q")
    return distinct


def compare_states(parent, child, states, alpha, distinct):
    p_delta = trans_output(parent.transitions, alpha)
    q_delta = trans_output(child.transitions, alpha)
    p_index = [s for s in states if s.name == p_delta].position
    q_index = [s for s in states if s.name == q_delta].position
    if distinct[q_index][p_index] != "X":
        return distinct[q_index][p_index]
    else:
        return None


def trans_output(transitions, alpha):
    output = transitions[[i for i,
                          j in enumerate(transitions)
                          if j[0] == 2][0]][-1]
    return output


def find_matches(distinct, states):
    matches = set()
    for col in range(len(distinct)):
        for row in range(len(distinct)):
            if distinct[row][col] == 0:
                p_state = [s for s in states if s.position == col]
                q_state = [s for s in states if s.position == row]
                sub_match = frozenset([p_state, q_state])
                matches.add(sub_match)
    return matches


def union_matches(matches, states):
    unions = set()
    for state in states:
        state_set = [s for s in matches if state.name in s]
        union_matches = set()
        for item in state_set:
            union_matches = union_matches.union(item)
        frozen_union = frozenset(union_matches)
        unions.add(frozen_union)
    return unions


def combine_states(unions, states):
    pre_trans_states = set()
    is_final = False
    is_start = False
    # Kind of pointless to note position at this point by why not track it
    position = 0
    for sub_sets in unions:
        if len(sub_sets) > 1:
            state_name = []
            state_trans = []
            for state in sub_sets:
                if state.is_start:
                    is_start = True
                if state.is_final:
                    is_final = True
                state_name.append(state.name)
                state_trans.append(state.transitions)
            pre_trans_state = State(
                state_name, is_start, is_final, None, position)
            pre_trans_states.add(pre_trans_state)
            position += 1
        else:
            x, = sub_sets
            new_state = [s for s in states if s.name == x]
            if len(new_state) != 0:
                print_error("MINIMIZING", "combine_states()",
                            "The singleton does not exist in the original states")
                return None
            new_state.position = position
            position += 1
            pre_trans_states.add(new_state)
    new_states = combine_trans(pre_trans_states, states)
    return new_states

# TODO States names NEED to be strings in order for this function to work


def combine_trans(pre_trans_states, states):
    new_states = []
    for pt_state in pre_trans_states:
        grouped_state = [s for s in states if set(pt_state.name).issuperset(s)]
        if len(grouped_state) == 1:
            new_transitions = [tuple(s[-1] if not set(s).issubset(pt_state.name)
                                     else pt_state.name for s in tup)
                               for tup in grouped_state]
            new_state = pt_state.transitions(new_transitions)
            new_states.append(new_state)
        elif len(grouped_state) > 1:
            new_transitions = [tuple(s[-1] if not set(s).issubset(pt_state.name)
                                     else pt_state.name for s in tup)
                               for tup in grouped_state[0]]
            new_state = pt_state.transitions(new_transitions)
            new_states.append(new_state)
        else:
            new_states.append(None)
            print_error("MINIMIZING", "combine_trans()",
                        "There was a problem grouping transition states")
    return new_states


def compare_table(distinct, old_distinct, states):
    is_changed = True
    if distinct == old_distinct:
        is_changed = False
    return is_changed


def print_table(distinct):
    print("EVENT: Printing table...")
    for row in reversed(distinct):
        print(row)
