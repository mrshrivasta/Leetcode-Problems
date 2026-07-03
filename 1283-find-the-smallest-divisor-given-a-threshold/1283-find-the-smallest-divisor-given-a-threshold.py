class Solution:
    def smallestDivisor(self, nums, threshold):
        def calc(d):
            return sum((x + d - 1) // d for x in nums)

        l, r = 1, max(nums)

        while l < r:
            mid = (l + r) // 2
            if calc(mid) <= threshold:
                r = mid
            else:
                l = mid + 1

        return l