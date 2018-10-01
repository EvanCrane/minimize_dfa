from src.dfa import Dfa

def prettyPrintMain(dfa):
    dfaList = []
    dfaList.append(states(dfa.states))
    dfaList.append(alpha(dfa.alpha))
    dfaList.append(trans(dfa.transfunc))
    dfaList.append(start(dfa.start))
    dfaList.append(final(dfa.final))
    print("Pretty printing DFA...")
    for str in dfaList:
        print(str)

def states(listObj):
    s1 = ','.join(listObj)
    str = '(states, (' + s1 + '))'
    return str

def alpha(listObj):
    s1 = ','.join(listObj)
    str = '(alpha, (' + s1 + '))'
    return str

def trans(listoflistObj):
    transList = []
    for l in listoflistObj:
        s1 = ','.join(l)
        transList.append('(' + s1 + ')')
    s2 = ','.join(transList)
    str = '(trans-func, (' + s2 + ')'
    return str

def start(strObj):
    str = '(start, ' + strObj + ')'
    return str

def final(listObj):
    s1 = ','.join(listObj)
    str = '(final, (' + s1 + '))'
    return str