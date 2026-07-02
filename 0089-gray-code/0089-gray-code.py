class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = [0]

        for i in range(n):
            for x in reversed(res):
                res.append(x | (1 << i))

        return res