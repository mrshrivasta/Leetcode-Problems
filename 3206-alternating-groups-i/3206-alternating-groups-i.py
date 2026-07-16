class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        n = len(colors)
        return sum(colors[(i-1)%n] != colors[i] and colors[(i+1)%n] != colors[i] for i in range(n))