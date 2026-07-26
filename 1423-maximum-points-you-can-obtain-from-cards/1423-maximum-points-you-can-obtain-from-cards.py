class Solution:
    def maxScore(self, cardPoints, k):
        n = len(cardPoints)

        if k == n:
            return sum(cardPoints)

        total = sum(cardPoints)
        window = n - k

        cur = sum(cardPoints[:window])
        mn = cur

        for i in range(window, n):
            cur += cardPoints[i] - cardPoints[i - window]
            mn = min(mn, cur)

        return total - mn