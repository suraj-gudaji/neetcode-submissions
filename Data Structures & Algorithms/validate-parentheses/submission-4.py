class Solution:
    def isValid(self, s: str) -> bool:

        x = {'(', '{', '['}
        stack = []

        if len(s) == 0:
            return True
        elif len(s) == 1:
            return False

        for i in s:

            if i not in x:
                if not stack:
                    return False
                elif i == ')' and stack[len(stack)-1] == '(':
                    stack.pop()
                elif i == ']' and stack[len(stack)-1] == '[':
                    stack.pop()
                elif i == '}' and stack[len(stack)-1] == '{':
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
                

        return len(stack) == 0
            
