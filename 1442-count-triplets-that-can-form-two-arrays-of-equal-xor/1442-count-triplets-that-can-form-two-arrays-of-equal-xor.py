class Solution:
    def countTriplets(self, arr):
        n = len(arr)
        ans = 0

        for i in range(n):
            x = 0
            for k in range(i, n):
                x ^= arr[k]
                if x == 0:
                    ans += k - i

        return ans