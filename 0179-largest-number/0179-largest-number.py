from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))
        nums.sort(key=cmp_to_key(lambda a, b: 1 if a+b < b+a else -1))
        result = "".join(nums)
        return "0" if result[0] == "0" else result