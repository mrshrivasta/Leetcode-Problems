from collections import Counter

class Solution:
    def countTriplets(self, nums: List[int]) -> int:
        and_count = Counter()

        for a in nums:
            for b in nums:
                and_count[a & b] += 1

        ans = 0

        for c in nums:
            for val, freq in and_count.items():
                if (val & c) == 0:
                    ans += freq

        return ans