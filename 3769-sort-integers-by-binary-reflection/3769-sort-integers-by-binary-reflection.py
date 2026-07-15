class Solution:
    def sortByReflection(self, nums: List[int]) -> List[int]:
        def reflect(x):
            return int(bin(x)[2:][::-1], 2)
        return sorted(nums, key=lambda x: (reflect(x), x))