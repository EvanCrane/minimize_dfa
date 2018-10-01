import src
from src.parse import parseMain
from src.prettyPrint import prettyPrintMain

def main():
    parsedDfa = parseMain()
    print("DFA PARSE RESULTS")
    print(parsedDfa.states)
    print(parsedDfa.alpha)
    print(parsedDfa.transfunc)
    print(parsedDfa.start)
    print(parsedDfa.final)
    print("Finished Main.....")
    prettyPrintMain(parsedDfa)
main()