class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        seen = set()
        pos, step = 0, 1
        while pos not in seen:
            seen.add(pos)
            pos = (pos + step * k) % n
            step += 1
        return [i for i in range(1, n+1) if (i-1) not in seen]