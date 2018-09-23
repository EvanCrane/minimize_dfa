import os
from dfa import Dfa

def parseMain():
    print("Running Main")
    fileLines = readFromFile()
    printText(fileLines)
    if verifyFileContent(fileLines):
        printDfaInput
        #parseDfaInput(fileLines)  
    else:
        print("Cannot use this file") 
    parsedDfa = "DFAs that are parsed"
    return parsedDfa

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

def printText(text):
    print(text)

def printDfaInput(states, alpha, transfunc, start, final):
    print(states + "/n" + alpha + "/n" + transfunc + "/n" + start + "/n" + final)  

def parseDfaStrings(stringList):
    dfaList = []
    for str in stringList:
        splitList = str.split(', ')
        first, rest = splitList[0], splitList[1:]
        content = rest[0][:-1]
        print(content)
        dfaList.append(content)
    dfa = Dfa()

def parseStates(stateStr):
    items = []
    for item in stateStr
        if item == '(':
            content, closeParen = 