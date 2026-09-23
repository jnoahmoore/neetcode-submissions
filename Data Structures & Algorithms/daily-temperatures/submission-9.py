class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp = temperatures
        res = [0] * len(temp)
        stack = []

        for index, tmp in enumerate(temp):
            while stack and stack[-1][0] < tmp:
                stack_prev_tmp,stack_prev_index = stack.pop()
                res[stack_prev_index] = index - stack_prev_index
            stack.append((tmp, index))
        
        return res    