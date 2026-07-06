from typing import List
from collections import Counter
from functools import lru_cache

class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        sticker_counts = [Counter(s) for s in stickers]

        @lru_cache(None)
        def dfs(rem):
            if not rem:
                return 0

            target_count = Counter(rem)
            ans = float('inf')

            for sticker in sticker_counts:
                # Optimization: sticker must contain first needed char
                if rem[0] not in sticker:
                    continue

                new_rem = []
                for ch, cnt in target_count.items():
                    if cnt > sticker[ch]:
                        new_rem.extend([ch] * (cnt - sticker[ch]))

                new_rem = ''.join(sorted(new_rem))
                res = dfs(new_rem)

                if res != -1:
                    ans = min(ans, 1 + res)

            return -1 if ans == float('inf') else ans

        return dfs(''.join(sorted(target)))