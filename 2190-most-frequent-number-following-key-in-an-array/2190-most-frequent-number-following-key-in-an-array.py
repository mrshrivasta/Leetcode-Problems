class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        c = Counter(nums[i+1] for i in range(len(nums)-1) if nums[i] == key)
        return max(c, key=c.get)