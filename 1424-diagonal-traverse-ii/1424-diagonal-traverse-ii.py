from collections import defaultdict

class Solution:
    def findDiagonalOrder(self, nums):
        diag = defaultdict(list)

        for r in range(len(nums)):
            for c in range(len(nums[r])):
                diag[r + c].append(nums[r][c])

        ans = []

        for k in sorted(diag):
            ans.extend(reversed(diag[k]))

        return ans