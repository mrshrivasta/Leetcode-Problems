class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        import heapq
        heap = [1]
        seen = {1}
        val = 1
        for _ in range(n):
            val = heapq.heappop(heap)
            for p in primes:
                nxt = val * p
                if nxt not in seen:
                    seen.add(nxt)
                    heapq.heappush(heap, nxt)
        return val