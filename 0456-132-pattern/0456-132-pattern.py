class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        num_2 = float('-inf')  # Tracks the best candidate for 'nums[k]' (the 2)
        
        # Iterate from right to left
        for num in reversed(nums):
            # If we find an element smaller than our '2', we found a '1'
            # Because num_2 is only set if a valid larger '3' exists to its left
            if num < num_2:
                return True
            
            # If the current number is greater than the stack's top,
            # it means the current number can act as a '3'.
            # We pop the stack to find the largest possible '2' for this '3'.
            while stack and num > stack[-1]:
                num_2 = stack.pop()
                
            # Push the current number as a candidate for '3'
            stack.append(num)
            
        return False