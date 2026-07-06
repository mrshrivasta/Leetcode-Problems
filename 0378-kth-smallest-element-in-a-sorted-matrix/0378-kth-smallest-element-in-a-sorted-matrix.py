class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        import heapq
        n = len(matrix)
        heap = [(matrix[i][0], i, 0) for i in range(n)]
        heapq.heapify(heap)
        for _ in range(k-1):
            val, r, c = heapq.heappop(heap)
            if c+1 < n:
                heapq.heappush(heap, (matrix[r][c+1], r, c+1))
        return heapq.heappop(heap)[0]