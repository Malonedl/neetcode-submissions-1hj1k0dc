class Solution:
    def isValid(self, s: str) -> bool:
        myStack = []
        if len(s) <= 1:
                return False

        for bracket in s:
            if len(myStack) == 0 and bracket in ')}]':
                return False
            
            elif bracket in '({[':
                myStack.append(bracket)
            
            elif bracket == ')' and myStack[-1] == '(':
                myStack.pop()
            
            elif bracket == ']' and myStack[-1] == '[':
                myStack.pop()

            elif bracket == '}' and myStack[-1] == '{':
                myStack.pop()
            
            else:
                return False
            
        if len(myStack) > 0:
                return False

        return True

            