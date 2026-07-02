from collections import defaultdict

class Solution:
    def numPairsDivisibleBy60(self, time):
        count = defaultdict(int)
        ans = 0

        for t in time:
            r = t % 60
            need = (60 - r) % 60

            ans += count[need]
            count[r] += 1

        return ans