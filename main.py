import src
from src.parse import parseMain

def main():
    parsedDfa = parseMain()
    print("DFA PARSE RESULTS")
    print(parsedDfa.states)
    print(parsedDfa.alpha)
    print(parsedDfa.transfunc)
    print(parsedDfa.start)
    print(parsedDfa.final)
    print("Finished Main.....")
main()