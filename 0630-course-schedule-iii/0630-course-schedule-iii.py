from typing import List
import heapq

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])

        total_time = 0
        max_heap = []

        for duration, lastDay in courses:
            total_time += duration
            heapq.heappush(max_heap, -duration)

            if total_time > lastDay:
                total_time += heapq.heappop(max_heap)

        return len(max_heap)