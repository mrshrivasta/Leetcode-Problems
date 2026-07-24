class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        total = 0
        n = len(arr)
        for i in range(n):
            for length in range(1, n - i + 1, 2):
                total += sum(arr[i:i+length])
        return total