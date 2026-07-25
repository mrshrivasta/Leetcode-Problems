from collections import Counter
from math import gcd
from functools import reduce

class Solution:
    def hasGroupsSizeX(self, deck):
        counts = Counter(deck).values()
        return reduce(gcd, counts) >= 2