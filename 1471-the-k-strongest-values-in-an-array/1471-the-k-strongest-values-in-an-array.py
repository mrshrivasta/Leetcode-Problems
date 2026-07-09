from typing import List

class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        n = len(arr)

        m = arr[(n - 1) // 2]

        left, right = 0, n - 1
        ans = []

        while len(ans) < k:
            if abs(arr[right] - m) >= abs(arr[left] - m):
                ans.append(arr[right])
                right -= 1
            else:
                ans.append(arr[left])
                left += 1

        return ans