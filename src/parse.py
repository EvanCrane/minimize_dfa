import os
from src.dfa import Dfa

def parseMain():
    print("Running Main")
    fileLines = readFromFile()
    print(fileLines)
    if verifyFileContent(fileLines):
        printDfaInput
        dfaList = parseDfaStrings(fileLines)  
        parsedDfa = Dfa(dfaList[0], dfaList[1], dfaList[2], dfaList[3], dfaList[4])
        return parsedDfa
    else:
        print("Cannot use this file") 

#Parse input from DFA file
def readFromFile():
    path = "test1.dfa"
    file = open(path, 'r')
    fileLines = file.readlines()
    file.close()
    return fileLines

def verifyFileContent(fileLines):
    if fileLines:
        if verifyFileDfaComponents(fileLines):
            print("Verified DFA components. Reading in values")
            return True
        else:
            print("File is missing needed content")
            return False
    else:
        print("There is nothing in the file") 
        return False

def verifyFileDfaComponents(fileLines):
    if (
        'states' in fileLines[0] and 'alpha' in fileLines[1] and
        'trans-func' in fileLines[2] and 'start' in fileLines[3] and 
        'final' in fileLines[4]
        ):
        print("Found DFA components")
        return True
    else:
        print("File is missing DFA components")
        return False

def printDfaInput(states, alpha, transfunc, start, final):
    print(states + "/n" + alpha + "/n" + transfunc + "/n" + start + "/n" + final)  

def parseDfaStrings(fileLines):
    dfaList = []
    propList = ['states','alpha','trans-func','start','final']
    linesWithProps = []
    
    print("LINES WITH PROPS")
    for str in fileLines:
        matchingLine = [x for x in propList if x in str]
        if len(matchingLine) > 0:
            linesWithProps.append(str)
    print(linesWithProps)
    for str in linesWithProps:
            splitList = str.split(', ')
            first, rest = splitList[0], splitList[1:]
            content = rest[0]
            content = content[:-2]
            if 'trans-func' in first:
                dfaList.append(parseListOfLists(content))
            elif 'start' in first:
                dfaList.append(content)
            elif 'states' in first or 'alpha' in first or 'final' in first:
                dfaList.append(parseList(content))        
    return dfaList

def parseList(content):
    if content.startswith('(') and content.endswith(')'):
        print("valid content in list")
        print(content)
        content = content.lstrip('(')
        content = content.rstrip(')')
        splitList = content.split(',')
        return splitList
    else:
        print("ERROR: invalid content in list") 
       
def parseListOfLists(content):
    stack = []
    def _helper(splitList):
        subStack = []
        for item in splitList:
            if "," in item:
                itemList = item.split(',')
                stack.append(_helper(itemList))
            else:
                subStack.append(item)
        return subStack  
    if content.startswith('(') and content.endswith(')'):
        print("valid content in list of lists")
        print(content)
        content = content.lstrip('(')
        content = content.rstrip(')')
        splitList = content.split('),(')
        print(splitList)
        _helper(splitList)
        return stack
    else:
        print("ERROR: invalid content in list") 