from src.dfa import Dfa


def verify_dfa_main(dfa):
    results = []
    results.append(verify_states(dfa.states))
    results.append(verify_alpha(dfa.alpha))
    results.append(verify_trans(dfa.transfunc, dfa.start,
                                dfa.final, dfa.states, dfa.alpha))
    results.append(verify_start(dfa.start, dfa.states))
    results.append(verify_final(dfa.final, dfa.states))
    if False in results:
        return False
    else:
        return True


def verify_states(states):
    return True


def verify_alpha(alpha):
    if len(alpha) > 1:
        return False
    else:
        return True


def verify_trans(trans, start, final, states, alpha):
    result = False
    # Compare trans to make sure they are in the states
    # Also compare trans to make sure that alphabet symbols are contained in alphabet
    for lst in trans:
        # Check if start state comes first
        for items in lst[0]:
            if start != items[0]:
                return False
        # Check if final state comes last
        for items in lst[-1]:
            if final != items[-1]:
                return False
        for items in lst:
            if len(items) == 3:
                if items[0] not in states or items[-1] not in states or items[1] not in alpha:
                    return False
                else:
                    result = True
            else:
                return False

    return result


def verify_start(start, states):
    if len(start) > 1 or start not in states:
        return False
    else:
        return True


def verify_final(final, states):
    if len(final) > 1 or final not in states:
        return False
    else:
        return True


def verify_state_objects_main(state_list):
    start_state = [s for s in state_list if s.is_start]
    if start_state == 1:
        return True
    return False
