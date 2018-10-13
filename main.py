import os
import sys
from pathlib import Path
from os.path import dirname, join
import src
from src.parse import parseMain
from src.parsefile import parse_main
from src.prettyPrint import pretty_print_main
from src.verify import verify_dfa_main
from src.minimize import minimize_main
from src.error import print_error


def main():
    print("Please enter the file from the test folder that you wish to run or type exit() to exit the program: ")
    file_path = input("file: ")
    if file_path == "exit()":
        print("EVENT: Exiting program...")
        exit(0)
    root_path = os.path.dirname(os.path.abspath(__file__))
    full_path = Path(root_path + "/test/" + file_path)
    if not full_path.is_file():
        print_error("FILE PATH", "main()",
                    "The file name provided is not a valid file")
        print("Please enter a valid file from the test folder\n")
        main()
    print("EVENT: Running main...")
    parsedDfa = parse_main(full_path)
    print("EVENT: DFA PARSE RESULTS")
    print(parsedDfa.states)
    print(parsedDfa.alpha)
    print(parsedDfa.transfunc)
    print(parsedDfa.start)
    print(parsedDfa.final)
    print("EVENT: Verifying DFA...")
    result = verify_dfa_main(parsedDfa)
    if result:
        dfa_min = minimize_main(parsedDfa)
        if dfa_min is None:
            print_error("MINIMIZE", "main()", "DFA cannot be minimized!!")
            print("EVENT: Finished Main.....")
            return exit(1)
        else:
            pretty_print_main(dfa_min)

    else:
        print_error("VERIFY", "main()", "DFA cannot be verified!!")
    print("EVENT: Finished Main.....")
    return exit(0)


main()
