class Dfa:
    def __init__(self, states, alpha, transfunc, start, final):
        self.states = states
        self.alpha = alpha
        self.transfunc = transfunc
        self.start = start
        self.final = final
    def defineDfa(self):
        print(vdir(self))