class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        deduped = [nums[0]]
        for x in nums[1:]:
            if x != deduped[-1]:
                deduped.append(x)
        count = 0
        for i in range(1, len(deduped)-1):
            if (deduped[i] > deduped[i-1] and deduped[i] > deduped[i+1]) or \
               (deduped[i] < deduped[i-1] and deduped[i] < deduped[i+1]):
                count += 1
        return count