from src.dfa import Dfa

def verifyDfaMain(dfa):
    results = []
    results.append(verifyStates(dfa.states))
    results.append(verifyAlpha(dfa.alpha))
    results.append(verifyTrans(dfa.transfunc, dfa.start, dfa.final, dfa.states, dfa.alpha))
    results.append(verifyStart(dfa.start, dfa.states))
    results.append(verifyFinal(dfa.final, dfa.states))
    if False in results:
        return False
    else:
        return True

def verifyStates(states):
    return True

def verifyAlpha(alpha):
    if len(alpha) > 1:
        return False
    else:
        return True

def verifyTrans(trans, start, final, states, alpha):
    result = False
    #Compare trans to make sure they are in the states
    #Also compare trans to make sure that alphabet symbols are contained in alphabet
    for lst in trans:
        #Check if start state comes first
        for items in lst[0]:
            if start != items[0]:
                return False
        #Check if final state comes last
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

def verifyStart(start, states):
    if len(start) > 1 or start not in states:
        return False
    else:
        return True
def verifyFinal(final, states):
    if len(final) > 1 or final not in states:
        return False
    else:
        return True
