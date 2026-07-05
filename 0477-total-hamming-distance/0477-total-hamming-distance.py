class Solution:
    def totalHammingDistance(self, nums: list[int]) -> int:
        total_dist = 0
        n = len(nums)
        
        # Since max value is 10^9, it fits well within a 32-bit integer framework
        for i in range(32):
            ones = 0
            # Count how many numbers have the i-th bit set
            for num in nums:
                if (num >> i) & 1:
                    ones += 1
            
            zeros = n - ones
            # The combination of (ones * zeros) gives pairs with different bits
            total_dist += ones * zeros
            
        return total_dist