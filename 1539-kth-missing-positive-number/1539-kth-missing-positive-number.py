class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        s = set(arr)
        count = 0
        num = 0
        while count < k:
            num += 1
            if num not in s:
                count += 1
        return num