class Solution:
    def maximumSum(self, arr):
        n = len(arr)

        keep = [0] * n
        drop = [0] * n

        keep[0] = arr[0]
        drop[0] = 0
        ans = arr[0]

        for i in range(1, n):
            keep[i] = max(arr[i], keep[i - 1] + arr[i])
            drop[i] = max(keep[i - 1], drop[i - 1] + arr[i])
            ans = max(ans, keep[i], drop[i])

        return ans