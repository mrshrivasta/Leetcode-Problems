class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        return [n for _, n in sorted(zip(heights, names), reverse=True)]