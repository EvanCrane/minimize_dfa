from src.dfa import Dfa


def pretty_print_main(dfa):
    dfaList = []
    dfaList.append(states(dfa.states))
    dfaList.append(alpha(dfa.alpha))
    dfaList.append(trans(dfa.transfunc, dfa.alpha))
    dfaList.append(start(dfa.start))
    dfaList.append(final(dfa.final))
    print("RESULT | PRETTY PRINTING MIN DFA...")
    for str in dfaList:
        print(str)


def states(listObj):
    s1 = ','.join(listObj)
    str = '(states, (' + s1 + '))'
    str = str.replace("'", "")
    return str


def alpha(listObj):
    s1 = ','.join(listObj)
    str = '(alpha, (' + s1 + '))'
    str = str.replace("'", "")
    return str


def trans(listoflistObj, alpha):
    transList = []
    i = 1
    for l in listoflistObj:
        if type(l) is list:
                s1 = ','.join(l)
                s1 = s1.replace("'","")
        else:
                s1 = l.replace("'","")
        if l == listoflistObj[-1]:
                transList.append('(' + s1 + ')')
                break
        transList.append('(' + s1 + '),')
        if i == len(alpha):
                transList.append('\n' + '\t\t')
                i = 0
        i += 1
    s2 = " ".join(transList)
    str = '(trans-func, (' + s2 + '))'
    return str


def start(strObj):
        if type(strObj) is list:
                s1 = ','.join(strObj)
                s1 = s1.replace("'","")
        else:
                s1 = strObj.replace("'","")
        str = '(start, ' + s1 + ')'
        str = str.replace("'", "")
        return str


def final(listObj):
    if len(listObj) > 0:
        s1 = ','.join(listObj)
        str = '(final, (' + s1 + '))'
        str = str.replace("'", "")
        return str
    else:
        str = '(final, ( ))'
        return str
