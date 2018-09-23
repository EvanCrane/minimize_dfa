class Dfa:
    def __init__(self, states, alpha, transfunc, start, final):
        self.states = states
        self.alpha = alpha
        self.transfunc = transfunc
        self.start = start
        self.final = final
    def printDfa(self):
        print(vdir(self))

def vdir(obj):
    return [x for x in dir(obj) if not x.startswith('__') and not x.startswith('print')]