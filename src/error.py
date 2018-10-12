class ErrorReport:
    def __init__(self, type, function, message):
        self.type = type
        self.function = function        
        self.message = message

    def print_obj(self):
        print("\n")
        print("ERROR | TYPE: " + self.type)
        print("FUNCTION: " + self.function)
        print("MESSAGE: " + self.message)
        print("END ERROR \n")

def print_error(type, function, message):
    e_obj = ErrorReport(type, function, message)
    e_obj.print_obj()