class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        def xsum(sub):
            c = Counter(sub)
            top = sorted(c.keys(), key=lambda v: (c[v], v), reverse=True)[:x]
            return sum(v * c[v] for v in top)
        return [xsum(nums[i:i+k]) for i in range(len(nums)-k+1)]