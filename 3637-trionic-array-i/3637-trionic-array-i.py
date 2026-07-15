class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        for p in range(1, n-2):
            for q in range(p+1, n-1):
                inc1 = all(nums[i] < nums[i+1] for i in range(p))
                dec = all(nums[i] > nums[i+1] for i in range(p, q))
                inc2 = all(nums[i] < nums[i+1] for i in range(q, n-1))
                if inc1 and dec and inc2:
                    return True
        return False