class Solution:
    def finalPrices(self, prices):
        stack, res = [], prices[:]
        for i, p in enumerate(prices):
            while stack and prices[stack[-1]] >= p:
                res[stack.pop()] -= p
            stack.append(i)
        return res