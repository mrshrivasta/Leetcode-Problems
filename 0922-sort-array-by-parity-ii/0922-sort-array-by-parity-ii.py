class Solution:
    def sortArrayByParityII(self, nums):
        res = [0] * len(nums)
        e, o = 0, 1
        for n in nums:
            if n % 2 == 0:
                res[e] = n
                e += 2
            else:
                res[o] = n
                o += 2
        return res