from collections import deque

class Solution:
    def shortestSubarray(self, nums: list[int], k: int) -> int:
        n = len(nums)
        # Create prefix sum array
        # prefix_sums[i] represents the sum of the first i elements
        prefix_sums = [0] * (n + 1)
        for i in range(n):
            prefix_sums[i + 1] = prefix_sums[i] + nums[i]
            
        # Deque will store indices of prefix_sums
        dq = deque()
        min_length = float('inf')
        
        for j in range(n + 1):
            # 1. Check if we found a valid subarray that meets the target sum K
            # If prefix_sums[j] - prefix_sums[dq[0]] >= k, we record the length
            # and pop from the left because we want the *shortest* subarray.
            while dq and prefix_sums[j] - prefix_sums[dq[0]] >= k:
                min_length = min(min_length, j - dq.popleft())
                
            # 2. Maintain the monotonicity of the deque.
            # If the current prefix sum is smaller than or equal to the last one in deque,
            # the older index is no longer useful. A smaller prefix sum at a later index
            # is always a better starting point for future valid subarrays.
            while dq and prefix_sums[j] <= prefix_sums[dq[-1]]:
                dq.pop()
                
            # Add current index to the deque
            dq.append(j)
            
        return min_length if min_length != float('inf') else -1