class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        n = len(arr)
        cut = n // 20
        return sum(arr[cut:-cut]) / (n - 2 * cut)