class Solution:
    def findRelativeRanks(self, score):
        ranks = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        order = sorted(range(len(score)), key=lambda x: -score[x])
        result = [""] * len(score)
        for i, idx in enumerate(order):
            result[idx] = ranks[i] if i < 3 else str(i + 1)
        return result