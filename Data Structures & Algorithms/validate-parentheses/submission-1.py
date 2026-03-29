class Solution:
    def isValid(self, s: str) -> bool:
        """
            Brute:


        """
        stack = []
        open_brackets = ["(", "[", "{"]

        for char in s:

            if char in open_brackets:
                stack.append(char)
            else:
                if len(stack) > 0:
                    if stack[-1] == "(" and char == ")":
                        stack.pop()
                    elif stack[-1] == "{" and char == "}":
                        stack.pop()
                    elif stack[-1] == "[" and char == "]":
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        
        if len(stack) == 0: 
            return True

        return False
                
        