class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        def score(p):
            return sum(2*p[i] if (i > 0 and p[i-1] == 10) or (i > 1 and p[i-2] == 10) else p[i] for i in range(len(p)))
        s1, s2 = score(player1), score(player2)
        return 1 if s1 > s2 else 2 if s2 > s1 else 0