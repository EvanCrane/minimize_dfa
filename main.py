import src
from src.parse import parseMain
from src.parsefile import parse_main
from src.prettyPrint import pretty_print_main
from src.verify import verify_dfa_main
from src.minimize import minimize_main


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
    result = verify_dfa_main(parsedDfa)
    if result:
        pretty_print_main(parsedDfa)
        print("EVENT: Finished Main.....")
    else:
        print("VERIFY ERROR: DFA cannot be verified!!")


def main2():
    print("EVENT: Running main2...")
    parsedDfa = parse_main()
    print("EVENT: DFA PARSE RESULTS")
    print(parsedDfa.states)
    print(parsedDfa.alpha)
    print(parsedDfa.transfunc)
    print(parsedDfa.start)
    print(parsedDfa.final)
    print("EVENT: Converting DFA to set of State Objects...")
    minimize_main(parsedDfa)


main2()
