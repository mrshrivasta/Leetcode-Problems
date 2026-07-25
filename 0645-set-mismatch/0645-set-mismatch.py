from collections import Counter

class Solution:
    def findErrorNums(self, nums):
        count = Counter(nums)
        dup = missing = 0
        for i in range(1, len(nums) + 1):
            if count[i] == 2: dup = i
            if count[i] == 0: missing = i
        return [dup, missing]