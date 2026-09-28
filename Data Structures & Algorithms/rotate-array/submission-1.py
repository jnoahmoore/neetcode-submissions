class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)

        self.reverse_arr(nums, 0, (len(nums) - 1))
        self.reverse_arr(nums,0, k - 1)
        self.reverse_arr(nums,k, (len(nums) - 1))

    def reverse_arr(self, nums, l, r):
        while l < r:
            nums[l], nums[r] = nums[r],nums[l]
            l, r = l + 1, r - 1