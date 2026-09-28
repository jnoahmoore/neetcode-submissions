class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            if s[i] != ']':
                stack.append(s[i])
            else:
                substr = ""
                while stack and stack[-1] != '[':
                    substr = stack.pop() + substr
                stack.pop()

                multiplier = ""
                while stack and stack[-1].isdigit():
                    multiplier = stack.pop() + multiplier
                    
                stack.append(int(multiplier) * substr)

        return "".join(stack)