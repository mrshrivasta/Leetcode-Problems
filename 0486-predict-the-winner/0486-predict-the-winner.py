class Solution:
    def predictTheWinner(self, nums):
        n = len(nums)

        def dfs(l, r):
            if l == r:
                return nums[l]

            pick_left = nums[l] - dfs(l + 1, r)
            pick_right = nums[r] - dfs(l, r - 1)

            return max(pick_left, pick_right)

        return dfs(0, n - 1) >= 0