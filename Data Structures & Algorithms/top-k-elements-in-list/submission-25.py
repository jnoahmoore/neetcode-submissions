class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for i in nums:
            count[i] = count.get(i, 0) + 1
 
        for index, num in count.items():
            freq[num].append(index)

        res = []

        for index in range(len(freq) - 1, -1, -1):
            for num in freq[index]:
                res.append(num)
                if len(res) == k:
                    return res