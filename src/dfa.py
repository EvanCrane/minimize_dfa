from src.verify import verify_state_objects_main

class Dfa:
    def __init__(self, states, alpha, transfunc, start, final):
        self.states = states
        self.alpha = alpha
        self.transfunc = transfunc
        self.start = start
        self.final = final

    def printDfa(self):
        print(vdir(self))

    def to_state_objects(self):
        states = []
        position = 0
        for state in self.states:
            is_start = False
            is_final = False
            if state == self.start:
                is_start = True
            if state in self.final:
                is_final = True
            trans_list = []
            for sublist in self.transfunc:
                if state in sublist[0]:
                    del sublist[0]
                    trans_list.append(sublist)
            state_obj = State(state, is_start, is_final, trans_list, position)
            states.append(state_obj)
            position += 1
        return states


class State:
    def __init__(self, name, is_start, is_final, transitions, position):
        self.name = name
        self.is_start = is_start
        self.is_final = is_final
        self.transitions = transitions
        self.position = position

    def printState(self):
        print(vdir(self))

    #def combine_states(self, combinations):
    #    for 
    #    return states

    

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

def states_to_dfa(state_list, alpha):
    if not (verify_state_objects_main(state_list)):
        return None
    else:
        states = []
        transfunc = []
        start = None
        final = []
        state_list.sort()
        start_state = [s for s in state_list if s.is_start]
        start = start_state.name
        states.append(start_state.name)
        for state in state_list:
            if state.is_start:
                break
            elif state.is_final:
                final.append(state.name)
            states.append(state.name)
            sub_trans = []
            for trans in state.transitions:
                sub_trans.append(state.name)
                sub_trans + list(trans)
                transfunc.append(sub_trans)


        dfa_min = Dfa(states, alpha, transfunc, start, final)
        return dfa_min

