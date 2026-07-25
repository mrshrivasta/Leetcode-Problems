class Solution:
    def canThreePartsEqualSum(self, arr):
        total = sum(arr)
        if total % 3 != 0:
            return False
        target, cur, parts = total // 3, 0, 0
        for n in arr:
            cur += n
            if cur == target:
                parts += 1
                cur = 0
        return parts >= 3