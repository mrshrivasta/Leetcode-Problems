class Solution:
    def countOppositeParity(self, nums: list[int]) -> list[int]:
        n = len(nums)
        odd = sum(x % 2 for x in nums)
        even = n - odd
        ans = []
        for x in nums:
            if x % 2:
                odd -= 1
                ans.append(even)
            else:
                even -= 1
                ans.append(odd)
        return ans