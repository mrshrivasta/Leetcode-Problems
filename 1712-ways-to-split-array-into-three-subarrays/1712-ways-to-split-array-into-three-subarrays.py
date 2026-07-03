class Solution:
    def waysToSplit(self, nums):
        MOD = 10**9 + 7
        n = len(nums)

        for i in range(1, n):
            nums[i] += nums[i - 1]

        ans = 0

        for i in range(n - 2):
            if nums[i] * 3 > nums[-1]:
                break

            l, r = i + 1, n - 2
            left, right = -1, -1

            while l <= r:
                mid = (l + r) // 2
                if nums[mid] - nums[i] >= nums[i]:
                    right = mid
                    r = mid - 1
                else:
                    l = mid + 1

            l, r = i + 1, n - 2
            while l <= r:
                mid = (l + r) // 2
                if nums[-1] - nums[mid] >= nums[mid] - nums[i]:
                    left = mid
                    l = mid + 1
                else:
                    r = mid - 1

            if left != -1 and right != -1 and right <= left:
                ans = (ans + (left - right + 1)) % MOD

        return ans