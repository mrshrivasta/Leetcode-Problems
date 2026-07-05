import heapq

class Solution:
    def mincostToHireWorkers(self, quality: list[int], wage: list[int], k: int) -> float:
        # Pair workers by their ratio of wage-to-quality and sort them by this ratio
        # ratio = wage / quality
        workers = sorted([(w / q, q) for q, w in zip(quality, wage)])
        
        min_cost = float('inf')
        quality_sum = 0
        max_heap = [] # Max-heap to track the largest qualities in our current pool
        
        for ratio, q in workers:
            # Add the current worker's quality to our selection pool
            heapq.heappush(max_heap, -q)
            quality_sum += q
            
            # If our pool exceeds size k, evict the worker with the highest quality
            if len(max_heap) > k:
                quality_sum += heapq.heappop(max_heap)
                
            # When we have exactly k workers, calculate the cost based on the current ratio
            if len(max_heap) == k:
                min_cost = min(min_cost, quality_sum * ratio)
                
        return min_cost