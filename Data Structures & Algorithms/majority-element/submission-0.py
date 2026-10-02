class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        res = 0

        for i in nums:
            count[i] = count.get(i, 0) + 1
        
        for key, val in count.items():
            if val > (len(nums) / 2):
                res = key

        return(res)