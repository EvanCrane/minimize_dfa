import src
from src.dfa import Dfa

def minimize_main(dfa):
    state_objs = dfa.to_state_objects
    distinct =  [[0 for x in range(len(state_objs))] for y in range(len(state_objs))]
    new_distinct = zero_equiv(state_objs, distinct)
    finished_distinct = n_equiv(new_distinct, None, state_objs)
    
    return dfa_min 

def zero_equiv(states_objs, distinct):
    finals = [f for f in states_objs
                if f.is_final is True]
    non_finals = [n for n in states_objs
                    if n.is_final is false]
    final_indexes = [i for i in finals.position]
    non_final_indexes = [i for i in non_finals.position]
    return set_the_table(distinct, final_indexes, non_final_indexes)
    
def set_the_table(distinct, final_indexes, non_final_indexes):
    completed_list = []
    for x in final_indexes:
        for y in non_final_indexes:
            complete = False
            for tup in completed_list:
                if x in tup and y in tup:
                    complete = True
                    break
            if complete is True:
                break
            distinct[x][y] = 1
    return distinct

def n_equiv(distinct, old_distinct, states):
    if distinct is None:
        #Were done here
        return old_distinct
    elif old_distinct is None:
        #do the first time loop
        new_distinct = update_table(distinct, states)
        n_equiv(new_distinct, distinct, states)
    else:
        #do all the other loops
        is_changed = compare_table(distinct, old_distinct, states)
        if  is_changed is True:
            new_distinct = update_table(distinct, states)
            n_equiv(new_distinct, distinct, states)
        else:
            n_equiv(None, distinct, states)
            

def update_table(distinct, states):
    completed_list = []
    for x in range(len(distinct)):
        for y in range(len(distinct[0])):
            complete = False
            if x == y 
                break
            if distinct[x][y] == 1:
                completed_list.append((x,y))
                break
            for tup in completed_list:
                if x in tup and y in tup:
                    complete = True
                    break
            if complete is True:
                break
            def _helper_compare(states[x], states[y], distinct[x][y], states)
            is_distinct = compare_states(distinct[x][y], states[x], states[y])
            completed_list.append((x,y))
            if is_distinct:
                distinct[x][y] = 1
            else:
                distinct[x][y] = 0
    return distinct           

def determine_distinct(parent, child, distinct, states):
    is_distinct = True
    if distinct_value != 1:
        

    return is_distinct


def compare_states(distinct_value, parent, child):
    is_distinct = True
    if distinct_value != 1:
        _helper_compare

    return is_distinct

def get_trans_output(state)

    return output
    
def find_similar_states(distinct):
    similar_states = []

    return similar_states


def compare_table(distinct, old_distinct, states):
    is_changed = True

    return is_changed