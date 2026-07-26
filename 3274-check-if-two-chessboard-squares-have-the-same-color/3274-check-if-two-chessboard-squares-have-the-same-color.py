class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        def color(c): return (ord(c[0]) + int(c[1])) % 2
        return color(coordinate1) == color(coordinate2)