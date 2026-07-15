class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        used = [False] * len(baskets)
        unplaced = 0
        for f in fruits:
            placed = False
            for j, b in enumerate(baskets):
                if not used[j] and b >= f:
                    used[j] = True
                    placed = True
                    break
            if not placed: unplaced += 1
        return unplaced