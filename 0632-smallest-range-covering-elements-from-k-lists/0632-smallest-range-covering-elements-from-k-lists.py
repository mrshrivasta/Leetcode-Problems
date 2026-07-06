from typing import List
import heapq

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        heap = []
        current_max = float('-inf')

        for i, arr in enumerate(nums):
            heapq.heappush(heap, (arr[0], i, 0))
            current_max = max(current_max, arr[0])

        start, end = -10**5, 10**5

        while True:
            current_min, row, col = heapq.heappop(heap)

            if current_max - current_min < end - start:
                start, end = current_min, current_max

            if col + 1 == len(nums[row]):
                break

            next_val = nums[row][col + 1]
            heapq.heappush(heap, (next_val, row, col + 1))
            current_max = max(current_max, next_val)

        return [start, end]