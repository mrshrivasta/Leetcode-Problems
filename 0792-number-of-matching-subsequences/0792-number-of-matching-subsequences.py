class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        # Map each char to sorted list of its indices in s
        char_indices = defaultdict(list)
        for i, c in enumerate(s):
            char_indices[c].append(i)

        def is_subseq(word):
            prev = -1
            for c in word:
                indices = char_indices[c]
                # Binary search for smallest index > prev
                lo, hi = 0, len(indices)
                while lo < hi:
                    mid = (lo + hi) // 2
                    if indices[mid] > prev:
                        hi = mid
                    else:
                        lo = mid + 1
                if lo == len(indices):
                    return False
                prev = indices[lo]
            return True

        return sum(is_subseq(w) for w in words)