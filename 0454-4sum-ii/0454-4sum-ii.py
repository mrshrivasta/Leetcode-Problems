from collections import Counter
from typing import List

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        # Hash map to store the frequencies of sums from nums1 and nums2
        sum_counts = Counter()
        
        # Step 1: Populate the map with all combinations of nums1[i] + nums2[j]
        for x in nums1:
            for y in nums2:
                sum_counts[x + y] += 1
                
        total_tuples = 0
        
        # Step 2: Check combinations of nums3[k] + nums4[l]
        for z in nums3:
            for w in nums4:
                target = -(z + w)
                # If the target exists in our map, add the number of occurrences
                if target in sum_counts:
                    total_tuples += sum_counts[target]
                    
        return total_tuples