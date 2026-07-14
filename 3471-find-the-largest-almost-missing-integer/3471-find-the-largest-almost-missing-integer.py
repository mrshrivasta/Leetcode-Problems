class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = {}
        for i in range(n - k + 1):
            for x in set(nums[i:i+k]):
                count[x] = count.get(x, 0) + 1
        res = [x for x, c in count.items() if c == 1]
        return max(res) if res else -1