class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        c, res = Counter(nums), 0
        for k, v in c.items():
            if v == 2: res ^= k
        return res