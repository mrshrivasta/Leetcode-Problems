class Solution:
    def canMakeArithmeticProgression(self, arr):
        arr.sort()
        return len(set(arr[i+1]-arr[i] for i in range(len(arr)-1))) == 1