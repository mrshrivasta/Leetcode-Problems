class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps       = 0
        current_end = 0   # rightmost index reachable with 'jumps' jumps
        farthest    = 0   # rightmost index reachable with 'jumps+1' jumps

        for i in range(len(nums) - 1):   # no jump needed from last index
            farthest = max(farthest, i + nums[i])

            if i == current_end:          # used up all positions in this level
                jumps      += 1
                current_end = farthest

        return jumps