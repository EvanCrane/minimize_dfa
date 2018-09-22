import src
from src.parse import parseMain

def main():
    parsedDfa = parseMain()
    return parsedDfa

def vdir(obj):
    return [x for x in dir(obj) if not x.startswith('__')]

class Dfa:
    def __init__(self, states, alpha, transfunc, start, final):
        self.states = states
        self.alpha = alpha
        self.transfunc = transfunc
        self.start = start
        self.final = final
    def defineDfa(self):
        print(vdir(self))

main()

dfa1 = Dfa("Test states", "Test alphabet", "Test transitions", "Test start", "Test final")

dfa1.defineDfa()