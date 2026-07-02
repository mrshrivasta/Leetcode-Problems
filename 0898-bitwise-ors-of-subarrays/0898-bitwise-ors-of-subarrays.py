class Solution:
    def subarrayBitwiseORs(self, arr):
        res = set()
        cur = set()

        for num in arr:
            cur = {num} | {x | num for x in cur}
            res |= cur

        return len(res)