from collections import Counter

class Solution:
    def repeatedNTimes(self, nums):
        return Counter(nums).most_common(1)[0][0]