from typing import List

class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        ans = []

        left, right = 1, k + 1

        while left <= right:
            ans.append(left)
            left += 1

            if left <= right:
                ans.append(right)
                right -= 1

        ans.extend(range(k + 2, n + 1))

        return ans