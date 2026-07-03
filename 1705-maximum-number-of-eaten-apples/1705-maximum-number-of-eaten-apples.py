import heapq

class Solution:
    def eatenApples(self, apples, days):
        heap = []
        n = len(apples)
        i = 0
        eaten = 0

        while i < n or heap:
            if i < n and apples[i] > 0:
                heapq.heappush(heap, (i + days[i], apples[i]))

            while heap and heap[0][0] <= i:
                heapq.heappop(heap)

            if heap:
                exp, cnt = heapq.heappop(heap)
                eaten += 1
                if cnt > 1:
                    heapq.heappush(heap, (exp, cnt - 1))

            i += 1

        return eaten