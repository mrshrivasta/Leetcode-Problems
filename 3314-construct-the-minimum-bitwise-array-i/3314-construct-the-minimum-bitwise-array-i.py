class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        res = []
        for p in nums:
            if p == 2:
                res.append(-1)
            else:
                found = -1
                for x in range(p):
                    if x | (x+1) == p:
                        found = x
                        break
                res.append(found)
        return res