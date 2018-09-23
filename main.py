import src
from src.parse import parseMain

def main():
    parsedDfa = parseMain()
    return parsedDfa

def vdir(obj):
    return [x for x in dir(obj) if not x.startswith('__')]

main()