import src
from src.dfa import Dfa
from src.error import print_error


def verify_dfa_main(dfa):
    results = []
    results.append(verify_states(dfa.states, dfa.start, dfa.final))
    results.append(verify_alpha(dfa.alpha))
    results.append(verify_trans(dfa.transfunc, dfa.start,
                                dfa.final, dfa.states, dfa.alpha))
    results.append(verify_start(dfa.start, dfa.states))
    results.append(verify_final(dfa.final, dfa.states))
    if False in results:
        print_error("VERIFY", "verify_dfa_main()", "Parsed DFA did not meet verification conditions")
        return False
    else:
        print("EVENT: Succesful DFA verification")
        return True


def verify_states(states, start, final):
    #At least 1
    # Verify that there are only alphanumeric characters
    # Verify that there are no duplicate states
    # Verify that states are a superset of start and final
    if (
        len(states) >= 1 and
        all(e.isalnum() for e in states) and
        len(states) == len(set(states)) and 
        set(states).issuperset(start) and 
        set(states).issuperset(final)
    ):
        return True
    else:
        print_error("VERIFY", "verify_states", "states do not meet the correct conditions")
        return False

def verify_alpha(alpha):
    if len(alpha) == 0:
        return True

    # Verify that alpha is alphanumeric
    # No duplicates
    if ( 
        len(alpha) >= 1 and
        all(e.isalnum() for e in alpha) and 
        len(alpha) == len(set(alpha))
    ):
        return True
    else:
        print_error("VERIFY", "verify_alpha", "alphas do not meet the correct conditions")
        return False


def verify_trans(trans, start, final, states, alpha):
    #Every transition head is a subset of the states
    #Every alphabet is in the alpha set
    #Every transition output is a member of the set of states
    #For each alphabet letter for a state there can only be one output per letter.
    #Start and final states need to exist 
    if len(trans) == 0:
        return True
    start_check = False
    final_check = False
    for items in trans:
        first = items[0]
        alph = items[1]
        last = items[-1]
        if (
            set(first).issubset(states) and 
            set(alph).issubset(alpha) and
            set(last).issubset(states)
        ):
            if set(first).issubset(first):
                start_check = True
        else:
            print_error("VERIFY", "verify_trans", "transitions do not meet the correct conditions")
            return False
    
    for state in states:
        for als in alpha:
            match = [a for a in trans if state in a[0] and als in a[1]]
        if len(match) == 1 and start_check:
            return True
        else:
            print_error("VERIFY", "verify_trans", "transitions do not meet the correct conditions")
            return False


def verify_start(start, states):
    # Verify that there is only one start state
    # Start state needs to be a subset of states
    # Start should be alphanumeric
    if (
        len(start) == 1 and
        start.isalnum() and 
        set(start).issubset(states)
    ):
        return True
    else:
        print_error("VERIFY", "verify_start", "start does not meet the correct conditions")
        return False


def verify_final(final, states):
    #Must not be empty
    #Alphanumeric
    #Final states must have no duplicates
    #Final states are a subset of states
    if len(final) > 0:
        if (
            len(final) >= 1 and 
            all(e.isalnum() for e in final) and
            len(final) == len(set(final)) and 
            set(final).issubset(states)
        ):
            return True
        else:
            print_error("VERIFY", "verify_final", "final does not meet the correct conditions")
            return False
    else:
        return True
