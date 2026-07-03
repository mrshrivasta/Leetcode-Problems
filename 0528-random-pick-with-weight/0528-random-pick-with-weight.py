import random
import bisect

class Solution:

    def __init__(self, w):
        self.prefix = []
        s = 0
        for x in w:
            s += x
            self.prefix.append(s)

    def pickIndex(self):
        target = random.randint(1, self.prefix[-1])
        return bisect.bisect_left(self.prefix, target)