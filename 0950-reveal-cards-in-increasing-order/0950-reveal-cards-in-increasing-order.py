from collections import deque

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        positions = deque(range(n))
        ans = [0] * n

        for card in sorted(deck):
            ans[positions.popleft()] = card

            if positions:
                positions.append(positions.popleft())

        return ans