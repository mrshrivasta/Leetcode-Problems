class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        def match(a, b):
            return sum(c1 == c2 for c1, c2 in zip(a, b))

        candidates = words[:]

        while candidates:
            # Pick the word that minimizes worst-case remaining candidates (minimax)
            guess = min(
                candidates,
                key=lambda w: max(
                    sum(match(w, c) == m for c in candidates)
                    for m in range(7)
                )
            )

            result = master.guess(guess)
            if result == 6:
                return

            candidates = [c for c in candidates if match(guess, c) == result]