class Solution:
    def largestGoodInteger(self, num: str) -> str:
        return max((num[i:i+3] for i in range(len(num)-2) if len(set(num[i:i+3])) == 1), default="")