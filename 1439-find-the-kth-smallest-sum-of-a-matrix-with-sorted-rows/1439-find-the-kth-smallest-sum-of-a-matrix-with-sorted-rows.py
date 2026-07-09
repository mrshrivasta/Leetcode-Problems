import heapq

class Solution:
    def kthSmallest(self, mat, k):
        cur = [0]

        for row in mat:
            heap = []

            for s in cur:
                for x in row:
                    heapq.heappush(heap, s + x)

            cur = heapq.nsmallest(k, heap)

        return cur[k - 1]