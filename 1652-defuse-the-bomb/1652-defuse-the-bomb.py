class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        res = []
        for i in range(n):
            if k == 0:
                res.append(0)
            elif k > 0:
                res.append(sum(code[(i+j) % n] for j in range(1, k+1)))
            else:
                res.append(sum(code[(i+j) % n] for j in range(k, 0)))
        return res