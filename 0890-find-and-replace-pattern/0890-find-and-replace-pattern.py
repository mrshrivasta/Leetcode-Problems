class Solution:
    def findAndReplacePattern(self, words, pattern):
        def match(word):
            w_to_p = {}
            p_to_w = {}

            for w, p in zip(word, pattern):
                if w in w_to_p and w_to_p[w] != p:
                    return False
                if p in p_to_w and p_to_w[p] != w:
                    return False

                w_to_p[w] = p
                p_to_w[p] = w

            return True

        return [word for word in words if match(word)]