from typing import List

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def can_split(max_sum):
            count = 1
            curr = 0

            for num in nums:
                if curr + num > max_sum:
                    count += 1
                    curr = num
                else:
                    curr += num

            return count <= k

        left, right = max(nums), sum(nums)

        while left < right:
            mid = (left + right) // 2

            if can_split(mid):
                right = mid
            else:
                left = mid + 1

        return left