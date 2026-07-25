class Solution:
    def relativeSortArray(self, arr1, arr2):
        order = {v: i for i, v in enumerate(arr2)}
        return sorted(arr1, key=lambda x: (order.get(x, len(arr2) + x)))