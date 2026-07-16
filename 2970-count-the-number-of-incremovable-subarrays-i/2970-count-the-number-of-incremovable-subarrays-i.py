class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        n, count = len(nums), 0
        for i in range(n):
            for j in range(i, n):
                rem = nums[:i] + nums[j+1:]
                if all(rem[k] < rem[k+1] for k in range(len(rem)-1)) or len(rem) <= 1:
                    count += 1
        return count