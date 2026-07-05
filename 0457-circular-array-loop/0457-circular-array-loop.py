class Solution:
    def circularArrayLoop(self, nums: list[int]) -> bool:
        n = len(nums)
        
        def get_next(curr: int) -> int:
            return (curr + nums[curr]) % n
        
        for i in range(n):
            if nums[i] == 0:
                continue
                
            slow = i
            fast = i
            is_forward = nums[i] > 0
            
            while True:
                # Move slow pointer 1 step
                if nums[slow] == 0 or (nums[slow] > 0) != is_forward:
                    break
                slow = get_next(slow)
                
                # Move fast pointer 1st step
                if nums[fast] == 0 or (nums[fast] > 0) != is_forward:
                    break
                fast = get_next(fast)
                
                # Move fast pointer 2nd step
                if nums[fast] == 0 or (nums[fast] > 0) != is_forward:
                    break
                fast = get_next(fast)
                
                if slow == fast:
                    # Check if cycle length is > 1
                    if slow == get_next(slow):
                        break  # Single-element loop, invalid
                    return True
            
            # Optimization: Safely mark all nodes in this invalid path as 0
            curr = i
            while nums[curr] != 0 and (nums[curr] > 0) == is_forward:
                nxt = get_next(curr)
                nums[curr] = 0
                curr = nxt
                
        return False