from typing import List

class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        # Window sums
        window = [0] * (n - k + 1)
        cur = sum(nums[:k])
        window[0] = cur

        for i in range(1, n - k + 1):
            cur += nums[i + k - 1] - nums[i - 1]
            window[i] = cur

        # Best left interval
        left = [0] * len(window)
        best = 0
        for i in range(len(window)):
            if window[i] > window[best]:
                best = i
            left[i] = best

        # Best right interval
        right = [0] * len(window)
        best = len(window) - 1
        for i in range(len(window) - 1, -1, -1):
            if window[i] >= window[best]:
                best = i
            right[i] = best

        ans = [-1, -1, -1]
        max_sum = 0

        # Middle interval
        for mid in range(k, len(window) - k):
            l = left[mid - k]
            r = right[mid + k]

            total = window[l] + window[mid] + window[r]

            if total > max_sum:
                max_sum = total
                ans = [l, mid, r]

        return ans