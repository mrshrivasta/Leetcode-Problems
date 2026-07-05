import heapq
from collections import defaultdict
from typing import List

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        # max_heap stores the smaller half (negated values for min-heap implementation)
        # min_heap stores the larger half
        max_heap = []
        min_heap = []
        
        # Track elements that need to be lazily deleted
        # {num: count_to_delete}
        lazy_deletions = defaultdict(int)
        
        # Balance tracker: size(max_heap) - size(min_heap)
        # We maintain: 0 <= balance <= 1
        balance = 0 
        
        def add_num(num):
            nonlocal balance
            if not max_heap or num <= -max_heap[0]:
                heapq.heappush(max_heap, -num)
                balance += 1
            else:
                heapq.heappush(min_heap, num)
                balance -= 1
            rebalance()

        def remove_num(num):
            nonlocal balance
            lazy_deletions[num] += 1
            if num <= -max_heap[0]:
                balance -= 1
            else:
                balance += 1
            rebalance()

        def rebalance():
            nonlocal balance
            # max_heap has too many elements
            while balance > 1:
                heapq.heappush(min_heap, -heapq.heappop(max_heap))
                balance -= 2
            # min_heap has too many elements
            while balance < 0:
                heapq.heappush(max_heap, -heapq.heappop(min_heap))
                balance += 2
                
            # Clean up invalid elements from tops of heaps
            prune_heaps()

        def prune_heaps():
            # Remove expired elements from the top of max_heap
            while max_heap and lazy_deletions[-max_heap[0]] > 0:
                lazy_deletions[-max_heap[0]] -= 1
                heapq.heappop(max_heap)
            # Remove expired elements from the top of min_heap
            while min_heap and lazy_deletions[min_heap[0]] > 0:
                lazy_deletions[min_heap[0]] -= 1
                heapq.heappop(min_heap)

        def get_median():
            if k % 2 == 1:
                return float(-max_heap[0])
            else:
                return (-max_heap[0] + min_heap[0]) / 2.0

        # Initialize the first window
        for i in range(k):
            add_num(nums[i])
            
        result = [get_median()]
        
        # Slide the window across the rest of the array
        for i in range(k, len(nums)):
            add_num(nums[i])             # Add incoming element
            remove_num(nums[i - k])       # Mark outgoing element for lazy deletion
            result.append(get_median())   # Get current median
            
        return result