class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ops = operations
        stack = []
        res = 0

        for i in ops:
            if i == '+':
                stack.append(stack[-1] + stack[-2])
            elif i == 'D':
                stack.append(stack[-1] * 2)
            elif i == 'C':
                stack.pop()
            else:
                stack.append(int(i))
        res = sum(stack)
        return res