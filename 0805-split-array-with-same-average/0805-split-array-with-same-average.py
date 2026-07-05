from typing import List

class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)

        # Quick feasibility check
        possible = False
        for k in range(1, n // 2 + 1):
            if total * k % n == 0:
                possible = True
                break

        if not possible:
            return False

        m = n // 2
        left = nums[:m]
        right = nums[m:]

        left_sums = [set() for _ in range(len(left) + 1)]
        left_sums[0].add(0)

        for num in left:
            for size in range(len(left), 0, -1):
                for s in left_sums[size - 1]:
                    left_sums[size].add(s + num)

        right_sums = [set() for _ in range(len(right) + 1)]
        right_sums[0].add(0)

        for num in right:
            for size in range(len(right), 0, -1):
                for s in right_sums[size - 1]:
                    right_sums[size].add(s + num)

        for k in range(1, n):
            if total * k % n:
                continue

            target = total * k // n

            for lsize in range(max(0, k - len(right)),
                               min(k, len(left)) + 1):
                rsize = k - lsize

                for lsum in left_sums[lsize]:
                    if target - lsum in right_sums[rsize]:
                        return True

        return False