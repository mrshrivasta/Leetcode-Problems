class Solution:
    def findLongestWord(self, s, dictionary):
        def is_subseq(word):
            i = 0
            for ch in s:
                if i < len(word) and word[i] == ch:
                    i += 1
            return i == len(word)

        best = ""

        for w in dictionary:
            if is_subseq(w):
                if len(w) > len(best) or (len(w) == len(best) and w < best):
                    best = w

        return best