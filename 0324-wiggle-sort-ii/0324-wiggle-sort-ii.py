class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        s = sorted(nums)
        n = len(nums)
        mid = (n-1)//2
        nums[::2] = s[mid::-1]
        nums[1::2] = s[n-1:mid:-1]