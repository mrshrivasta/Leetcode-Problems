class Solution:
    def longestMountain(self, arr: list[int]) -> int:
        n = len(arr)
        max_length = 0
        base = 0
        
        # A mountain requires at least 3 elements
        while base < n - 2:
            end = base
            
            # 1. Step forward along the upslope (if it exists)
            if end + 1 < n and arr[end] < arr[end + 1]:
                while end + 1 < n and arr[end] < arr[end + 1]:
                    end += 1
                
                # 'end' is now at a potential peak. 
                # 2. Step forward along the downslope (must exist)
                if end + 1 < n and arr[end] > arr[end + 1]:
                    while end + 1 < n and arr[end] > arr[end + 1]:
                        end += 1
                    
                    # We found a complete mountain from 'base' to 'end'
                    max_length = max(max_length, end - base + 1)
                    
                    # The end of this mountain can be the start of the next
                    base = end
                else:
                    # No downslope followed the peak, move base past the flat/upslope peak
                    base = end
            else:
                # No upslope found, shift base by 1
                base += 1
                
        return max_length