from collections import defaultdict

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        n   = len(s)
        k   = len(words)       # number of words needed
        w   = len(words[0])    # fixed word length
        total = k * w          # total window character length

        word_count = defaultdict(int)
        for word in words:
            word_count[word] += 1

        result = []

        # Run a separate sliding window for each starting offset 0..w-1
        for offset in range(w):
            window = defaultdict(int)
            matched = 0          # words correctly placed in window
            left = offset        # left boundary of window (in word units)

            for right in range(offset, n - w + 1, w):
                word = s[right: right + w]

                if word in word_count:
                    window[word] += 1
                    matched += 1

                    # Shrink from left while this word is over-represented
                    while window[word] > word_count[word]:
                        left_word = s[left: left + w]
                        window[left_word] -= 1
                        matched -= 1
                        left += w

                    if matched == k:
                        result.append(left)
                        # Slide left by one word to look for next valid window
                        left_word = s[left: left + w]
                        window[left_word] -= 1
                        matched -= 1
                        left += w
                else:
                    # Unknown word — reset window entirely from here
                    window.clear()
                    matched = 0
                    left = right + w

        return result