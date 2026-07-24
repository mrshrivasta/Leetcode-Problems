class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        n = len(arr)
        for i in range(n - m * k + 1):
            pattern = arr[i:i+m]
            if pattern * k == arr[i:i+m*k]:
                return True
        return False