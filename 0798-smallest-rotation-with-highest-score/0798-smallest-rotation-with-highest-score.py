from typing import List

class Solution:
    def bestRotation(self, nums: List[int]) -> int:
        n = len(nums)
        change = [0] * (n + 1)

        for i, num in enumerate(nums):
            left = (i - num + 1 + n) % n
            right = (i + 1) % n

            change[left] -= 1
            change[right] += 1

            if left > right:
                change[0] -= 1

        best_k = 0
        score = 0
        max_score = -n

        for k in range(n):
            score += change[k]

            if score > max_score:
                max_score = score
                best_k = k

        return best_k