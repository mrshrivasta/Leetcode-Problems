class Solution:
    def numFactoredBinaryTrees(self, arr: list[int]) -> int:
        MOD = 10**9 + 7
        
        # Sort the array so we process smaller numbers first
        arr.sort()
        
        # dp map where key = node value, value = number of valid trees rooted at this value
        dp = {}
        
        for i, parent in enumerate(arr):
            # Base case: The single-node tree consisting of just the parent itself
            ways = 1
            
            # Look for factors among the elements smaller than the current parent
            for j in range(i):
                left = arr[j]
                
                # Since the array is sorted, if left * left > parent, 
                # no further distinct pairs can form this parent.
                if left * left > parent:
                    break
                
                # Check if 'left' is a clean divisor of 'parent'
                if parent % left == 0:
                    right = parent // left
                    
                    # If the matching 'right' factor is also present in our array
                    if right in dp:
                        # If the children are distinct, we have two orientations (left/right swap)
                        if left != right:
                            ways = (ways + dp[left] * dp[right] * 2) % MOD
                        # If the children are identical, swapping gives the same tree
                        else:
                            ways = (ways + dp[left] * dp[right]) % MOD
                            
            # Store the computed total ways for this parent node
            dp[parent] = ways
            
        # The answer is the sum of ways to form trees rooted at *any* element in the array
        return sum(dp.values()) % MOD