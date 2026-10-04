class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        for r in range(1, len(nums)):
            # print(f"Before Nums: {nums}, L: {l}:{nums[l]}, R: {r}:{nums[r]}")
            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]
                l += 1
            # print(f"After Nums: {nums}, L: {l}:{nums[l]}, R: {r}:{nums[r]}")
        return l