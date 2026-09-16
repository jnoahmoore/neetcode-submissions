class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxNum = []
        queue = deque() #index
        l = 0
        r = 0

        while r < len(nums):
            while queue and nums[queue[-1]] < nums[r]:
                queue.pop()
            queue.append(r)
            
            #remove left val from window
            if l > queue[0]:
                queue.popleft()

            if (r + 1) >= k:
                maxNum.append(nums[queue[0]])
                l += 1
            r += 1

        return maxNum
        
        # maxNum = []
        # l = 0

        # for r in range(len(nums)):
        #     while (r - l + 1) > k:
        #         l += 1
        #     while (r - l + 1) == k:
        #         maxNum.append(max(nums[l:r + 1]))
        #         l += 1
            
        # return maxNum