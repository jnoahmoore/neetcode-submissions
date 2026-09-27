class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)

        if n1 > n2:
            return False
        
        string_1 = [0] * 26
        string_2 = [0] * 26

        for i in range(n1):
            string_1[ord(s1[i]) - ord('a')] += 1
            string_2[ord(s2[i]) - ord('a')] += 1
        if string_1 == string_2:
            return True
        
        for i in range(n1, n2):
            string_2[ord(s2[i]) - ord('a')] += 1
            string_2[ord(s2[i - n1]) - ord('a')] -= 1
            if string_1 == string_2:
                return True
        return False