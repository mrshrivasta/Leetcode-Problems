class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def get_groups(t):
            # Returns list of (char, count) groups
            groups = []
            i = 0
            while i < len(t):
                c, j = t[i], i
                while j < len(t) and t[j] == c:
                    j += 1
                groups.append((c, j - i))
                i = j
            return groups

        def is_stretchy(word):
            sg = get_groups(s)
            wg = get_groups(word)
            if len(sg) != len(wg):
                return False
            for (sc, sn), (wc, wn) in zip(sg, wg):
                if sc != wc:
                    return False
                # s group must be >= word group, and either already >=3 or exact match
                if sn < wn or (sn != wn and sn < 3):
                    return False
            return True

        return sum(is_stretchy(w) for w in words)