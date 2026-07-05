from typing import List

class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        def count(bound):
            ans = 0
            cur = 0

            for num in nums:
                if num <= bound:
                    cur += 1
                else:
                    cur = 0

                ans += cur

            return ans

        return count(right) - count(left - 1)