class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        count = [0] * 101
        for b, d in logs:
            for y in range(b, d):
                count[y - 1950] += 1
        return 1950 + count.index(max(count))