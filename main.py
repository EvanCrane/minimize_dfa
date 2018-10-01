import src
from src.parse import parseMain
from src.prettyPrint import prettyPrintMain
from src.verifyDfa import verifyDfaMain

def main():
    parsedDfa = parseMain()
    print("DFA PARSE RESULTS")
    print(parsedDfa.states)
    print(parsedDfa.alpha)
    print(parsedDfa.transfunc)
    print(parsedDfa.start)
    print(parsedDfa.final)
    print("Verifying DFA...")
    result = verifyDfaMain(parsedDfa)
    if result:
        prettyPrintMain(parsedDfa)
        print("Finished Main.....")
    else:
        print("DFA cannot be verified!!")

main()