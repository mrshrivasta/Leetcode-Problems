class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for n in nums: xor ^= n
        bit = xor & (-xor)
        a = b = 0
        for n in nums:
            if n & bit: a ^= n
            else: b ^= n
        return [a, b]