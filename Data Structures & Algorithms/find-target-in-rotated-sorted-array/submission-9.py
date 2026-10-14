class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l+r) // 2

            if nums[mid] == target:
                return mid

            # left sorted portion
            if nums[mid] >= nums[l]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            # right sorted portion
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1
            






        #     if nums[l] < nums[r]:
        #         if nums[mid] > target:
        #             r = mid - 1
        #         if nums[mid] < target:
        #             l = mid + 1
            
        #     if nums[mid] >= nums[l] and target < nums[l]:
        #         l = mid + 1
        #     else:
        #         r = mid - 1
            
        # return res