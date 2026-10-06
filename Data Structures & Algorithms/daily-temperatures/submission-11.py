class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp = temperatures
        stack = []
        res = [0] * len(temp)

        for index, tmp in enumerate(temp):
            while stack and stack[-1][0] < tmp:
                stack_tmp, stack_index = stack.pop()
                res[stack_index] = index - stack_index
            stack.append((tmp, index))
        
        return res