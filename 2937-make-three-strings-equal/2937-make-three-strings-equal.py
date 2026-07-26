class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        i = 0
        while i < min(len(s1), len(s2), len(s3)) and s1[i] == s2[i] == s3[i]:
            i += 1
        if i == 0:
            return -1
        return (len(s1) - i) + (len(s2) - i) + (len(s3) - i)