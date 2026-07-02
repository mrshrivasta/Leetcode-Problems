import random
from collections import defaultdict

class RandomizedCollection:

    def __init__(self):
        self.nums = []
        self.pos = defaultdict(set)

    def insert(self, val: int) -> bool:
        present = len(self.pos[val]) > 0

        self.nums.append(val)
        self.pos[val].add(len(self.nums) - 1)

        return not present

    def remove(self, val: int) -> bool:
        if not self.pos[val]:
            return False

        remove_idx = self.pos[val].pop()
        last_val = self.nums[-1]

        self.nums[remove_idx] = last_val

        if remove_idx != len(self.nums) - 1:
            self.pos[last_val].add(remove_idx)
            self.pos[last_val].remove(len(self.nums) - 1)

        self.nums.pop()

        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)