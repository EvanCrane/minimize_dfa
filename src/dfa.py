class Dfa:
    def __init__(self, states, alpha, transfunc, start, final):
        self.states = states
        self.alpha = alpha
        self.transfunc = transfunc
        self.start = start
        self.final = final

    def printDfa(self):
        print(vdir(self))


class State:
    def __init__(self, name, is_start, is_final, transitions):
        self.name = name
        self.is_start = is_start
        self.is_final = is_final
        self.transitions = transitions

    def printState(self):
        print(vdir(self))

class MinSet:
    def __init__(self, designation, number, states, has_start, has_final):
        self.designation = designation
        self.number = number
        self.has_start = has_start
        self.has_final = has_final
        self.states = states

    def printMinSet(self):
        print(vdir(self))


def vdir(obj):
    return [x for x in dir(obj) if not x.startswith('__') and not x.startswith('print')]

def dfa_to_state_set(dfa):
    states = set()
    for state in dfa.states:
        is_start = False
        is_final = False
        if state == dfa.start:
            is_start = True
        if state in dfa.final:
            is_final = True
        trans_list = []
        for sublist in dfa.transfunc:
            if state in sublist[0]:
                del sublist[0]
                trans_list.append(sublist)
        state_obj = State(state, is_start, is_final, trans_list)
        states.add(state_obj)
    return states