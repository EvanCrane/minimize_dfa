import src
from src.parse import parseMain
from src.parsefile import parse_main
from src.prettyPrint import pretty_print_main
from src.verifyDfa import verifyDfaMain


def main():
    print("EVENT: Running main...")
    parsedDfa = parse_main()
    print("EVENT: DFA PARSE RESULTS")
    print(parsedDfa.states)
    print(parsedDfa.alpha)
    print(parsedDfa.transfunc)
    print(parsedDfa.start)
    print(parsedDfa.final)
    print("EVENT: Verifying DFA...")
    result = verifyDfaMain(parsedDfa)
    if result:
        pretty_print_main(parsedDfa)
        print("EVENT: Finished Main.....")
    else:
        print("VERIFY ERROR: DFA cannot be verified!!")


main()
