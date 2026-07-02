class Solution:
    def limitOccurrences(self, nums: List[int], k: int) -> List[int]:
        res = []

        for num in nums:
            if len(res) < k or res[-k] != num:
                res.append(num)

        return res