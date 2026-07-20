class Solution:
    def lastVisitedIntegers(self, nums: List[int]) -> List[int]:
        seen, ans, k = [], [], 0
        for x in nums:
            if x != -1:
                seen.insert(0, x)
                k = 0
            else:
                k += 1
                ans.append(seen[k-1] if k <= len(seen) else -1)
        return ans