from typing import List
from collections import Counter

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        cnt = Counter(x % k for x in arr)

        if cnt[0] % 2:
            return False

        for r in range(1, k):
            if r == k - r:
                if cnt[r] % 2:
                    return False
            else:
                if cnt[r] != cnt[k - r]:
                    return False

        return True