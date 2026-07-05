class Solution:
    def advantageCount(self, nums1: list[int], nums2: list[int]) -> list[int]:
        n = len(nums1)
        # Sort nums1 in ascending order
        nums1.sort()
        
        # Sort nums2 elements by value in descending order, keeping track of original indices
        # Each element is (value, original_index)
        sorted_nums2 = sorted([(val, i) for i, val in enumerate(nums2)], reverse=True)
        
        # Initialize the result array with placeholder values
        res = [0] * n
        
        # Two pointers for the smallest and largest remaining elements in nums1
        left = 0
        right = n - 1
        
        # Process nums2 from largest value to smallest value
        for val, idx in sorted_nums2:
            # If our largest remaining element can beat the current largest nums2 element
            if nums1[right] > val:
                res[idx] = nums1[right]
                right -= 1
            # Otherwise, sacrifice our smallest remaining element
            else:
                res[idx] = nums1[left]
                left += 1
                
        return res