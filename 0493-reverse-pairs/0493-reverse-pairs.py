class Solution:
    def reversePairs(self, nums: list[int]) -> int:
        def merge_sort(low: int, high: int) -> int:
            if low >= high:
                return 0
            
            mid = (low + high) // 2
            count = merge_sort(low, mid) + merge_sort(mid + 1, high)
            
            # Count reverse pairs between left and right sorted halves
            count += count_pairs(low, mid, high)
            
            # Standard merge step to keep the array sorted
            merge(low, mid, high)
            
            return count

        def count_pairs(low: int, mid: int, high: int) -> int:
            right = mid + 1
            pairs = 0
            # For each element in the left half, find how many elements 
            # in the right half satisfy the condition
            for left in range(low, mid + 1):
                while right <= high and nums[left] > 2 * nums[right]:
                    right += 1
                pairs += (right - (mid + 1))
            return pairs

        def merge(low: int, mid: int, high: int):
            temp = []
            left = low
            right = mid + 1
            
            while left <= mid and right <= high:
                if nums[left] <= nums[right]:
                    temp.append(nums[left])
                    left += 1
                else:
                    temp.append(nums[right])
                    right += 1
                    
            while left <= mid:
                temp.append(nums[left])
                left += 1
                
            while right <= high:
                temp.append(nums[right])
                right += 1
                
            for i in range(len(temp)):
                nums[low + i] = temp[i]

        return merge_sort(0, len(nums) - 1)