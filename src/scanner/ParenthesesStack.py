class ParenthesesStack:
    def __init__(self):
        self.stack = []

    def push(self, parenthesis: str):
        if(parenthesis == "("):
            self.stack.append(parenthesis)
        elif(parenthesis == ")"):
            if(len(self.stack) == 0):
                raise Exception
            
            last = self.stack.pop()
            
            if(last == ")"):
                raise Exception("")
        else: 
            raise Exception("Cannot add something which not is a parenthesis in ParenthesesStack.")

    def isEmpty(self):
        return len(self.stack) == 0
    
    def clear(self):
        self.stack.clear()
    