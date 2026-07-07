class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        def bt(start, curr, rem):
            if len(curr) == k and rem == 0:
                res.append(curr[:])
                return
            for i in range(start, 10):
                if i > rem: break
                curr.append(i)
                bt(i+1, curr, rem-i)
                curr.pop()
        bt(1, [], n)
        return res