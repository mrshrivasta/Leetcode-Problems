class Solution:
    def findSpecialInteger(self, arr):
        threshold = len(arr) // 4
        for i in range(len(arr) - threshold):
            if arr[i] == arr[i + threshold]:
                return arr[i]