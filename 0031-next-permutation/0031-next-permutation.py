class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)

        # Step 1: Find the rightmost index i where nums[i] < nums[i+1]
        #         (the last "ascending pair" from the right)
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            # Step 2: Find the rightmost index j > i where nums[j] > nums[i]
            #         (smallest number in the suffix that beats nums[i])
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1

            # Step 3: Swap them
            nums[i], nums[j] = nums[j], nums[i]

        # Step 4: Reverse suffix from i+1 onward
        #         (suffix is descending after the swap → reverse = smallest order)
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left  += 1
            right -= 1