#minimize.py
import src
from src.error import print_error
from src.dfa import Dfa

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
    #states_min = 
    #dfa_min = 
    #return dfa_min 

def initialize_table(length):
    #Initialize 2d array entirely with X's initially
    if length == 1:
        table = ["X"]
        return table
    elif length > 1:
        table =  [['X' for x in range(length)] for y in range(length)]
        completed_list = []
        for col in table:
            for row in table:
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
                completed_list.append((col,row))
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
    completed_list = []    
    for f in final_indexes:
        for n in non_final_indexes:
            if distinct[f][n] == 'X':
                break
            complete = False
            for tup in completed_list:
                if f in tup and n in tup:
                    complete = True
                    break
            if complete is True:
                break
            distinct[f][n] = 1
            completed_list.append(f,n)
    return distinct

def n_equiv(distinct, alphas, states):
        #do the first time loop
        a_index = 0
        new_distinct = update_table(distinct, states, alphas[a_index])
        a_index += 1
        return _helper_equiv(new_distinct, a_index)
        print_error("MINIMIZE", "n_equiv",
            "Problem with input. Something is None where it shouldn't be and/or vice versa")

    def _helper_equiv(distinct, a_index):
        nonlocal alphas
        nonlocal states
        if a_index is not None:
            #do all the other loops
            if a_index < len(alphas):
                new_distinct = update_table(distinct, states, alphas[a_index])
                a_index += 1
                _helper_equiv(new_distinct, a_index)
            else:
                _helper_equiv(distinct, None)
        else:
            #Were done here
            return distinct
            

def update_table(distinct, states, alpha):
    completed_list = []
    for col in range(len(distinct)):
        for row in range(len(distinct)):
            complete = False
            if col == row or distinct[row][col] == 'X': 
                break
            if distinct[row][col] == 1:
                completed_list.append((col,row))
                break
            for tup in completed_list:
                if col in tup and row in tup:
                    complete = True
                    break
            if complete is True:
                break
            is_distinct = compare_states(distinct[row][col], 
                states.position == col, states.position == row)
            completed_list.append((col,row))
            if is_distinct:
                distinct[row][col] = 1
            else:
                distinct[row][col] = 0
    return distinct           

def determine_distinct(parent, child, distinct, states):
    is_distinct = True
        

    return is_distinct


def compare_states(distinct_value, parent, child):
    is_distinct = True
    p_delta = get_trans_output(parent)
    q_delta = get_trans_output(child)
    if distinct_value == 0 and dis:

    return is_distinct

def compare2(distinct, p, q):
    is_distinct = distinct[q][p]
    if is_distinct != 'X':
        return is_distinct
    else:
        return None
        print_error("MINIMIZE", "compare2()", 
            "Problem comparing states. There was a state reflection issue")
        

def get_trans_output(state):
    output = []
    return output
    
def find_similar_states(distinct):
    similar_states = []

    return similar_states

def compare_table(distinct, old_distinct, states):
    is_changed = True
    if distinct == old_distinct:
        is_changed = False
    return is_changed

def print_table(distinct):
    print("EVENT: Printing table...")
    for row in reversed(distinct):
        print(row)