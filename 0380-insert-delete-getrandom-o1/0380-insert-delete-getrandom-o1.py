class RandomizedSet:
    def __init__(self):
        self.idx = {}
        self.nums = []

    def insert(self, val: int) -> bool:
        if val in self.idx: return False
        self.idx[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.idx: return False
        i = self.idx[val]
        last = self.nums[-1]
        self.nums[i] = last
        self.idx[last] = i
        self.nums.pop()
        del self.idx[val]
        return True

    def getRandom(self) -> int:
        import random
        return random.choice(self.nums)