class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        longest = 0
        hashmap = set()

        for r in range(len(s)):
            while s[r] in hashmap:
                hashmap.remove(s[l])
                l += 1
            hashmap.add(s[r])
            longest = max(longest, r - l + 1)
        return longest