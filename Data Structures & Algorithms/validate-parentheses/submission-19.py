class Solution:
    def isValid(self, s: str) -> bool:
        my_dict = {"}":"{", "]":"[", ")":"("}
        stack = []

        for c in s:
            if c in my_dict:
                if stack and stack[-1] == my_dict[c]:
                    stack.pop()
                else:
                    return False
            else:    
                stack.append(c)

        return not stack
