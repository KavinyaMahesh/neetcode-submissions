class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        mp={")":"(","]":"[", "}":"{"}

        for c in s:
            #in map means it is a closing bracket
            if c in mp:
                #if stack is not empty and top of stack matches the bracket
                if stack and stack[-1]==mp[c]:
                    stack.pop()

                else:
                    return False
            # not in map which means its an opening bracket
            else:
                stack.append(c)     
        #return true if stack is empty else false
        return True if not stack else False            

        