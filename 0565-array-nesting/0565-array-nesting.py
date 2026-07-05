class Solution:
    def arrayNesting(self, nums):
        visited = set()
        ans = 0

        for i in range(len(nums)):
            if i not in visited:
                cnt = 0
                j = i
                while j not in visited:
                    visited.add(j)
                    j = nums[j]
                    cnt += 1
                ans = max(ans, cnt)

        return ans