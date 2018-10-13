


class Dfa:
    def __init__(self, states, alpha, transfunc, start, final):
        self.states = states
        self.alpha = alpha
        self.transfunc = transfunc
        self.start = start
        self.final = final

    def __copy__(self):
        return Dfa(self.states, self.alpha, self.transfunc,
                   self.start, self.final)

    def print_dfa(self):
        print(vdir(self))


class State:
    def __init__(self, name, is_start, is_final, transitions, position):
        self.name = name
        self.is_start = is_start
        self.is_final = is_final
        self.transitions = transitions
        self.position = position

    def print_state(self):
        print(vdir(self))


def vdir(obj):
    return [x for x in dir(obj) if not x.startswith('__') and not x.startswith('print')]


def dfa_to_states(d_states, d_trans, d_start, d_final):
    states = []
    position = 0
    for state in d_states:
        is_start = False
        is_final = False
        if state == d_start:
            is_start = True
        if state in d_final:
            is_final = True
        trans_list = []
        for sub_list in d_trans:
            if state in sub_list[0]:
                sublist = sub_list[1:]
                trans_list.append(sublist)
        state_obj = State(state, is_start, is_final, trans_list, position)
        states.append(state_obj)
        position += 1
    return states


def states_to_dfa(state_list, alpha):
    import operator
    states = []
    transfunc = []
    start = None
    final = []
    state_list.sort(key=operator.attrgetter('position'))
    start_state = [s for s in state_list if s.is_start]
    start = start_state[0].name
    str_start_name = str(start_state[0].name)
    states.append(str_start_name)
    for state in state_list:
        str_name = str(state.name)
        if state.is_final:
            final.append(str_name)
        if not state.is_start:
            states.append(str_name)
        for trans in state.transitions:
            sub_trans = []
            sub_trans.append(state.name)
            sub_trans += list(trans)
            transfunc.append(str(sub_trans))

    dfa_min = Dfa(states, alpha, transfunc, start, final)
    return dfa_min
