class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        queue = deque([(s1, 0)])
        visited = {s1}

        while queue:
            curr, swaps = queue.popleft()

            if curr == s2:
                return swaps

            # Find first mismatch position
            i = 0
            while curr[i] == s2[i]:
                i += 1

            # Try swapping with every valid candidate to the right
            for j in range(i + 1, len(curr)):
                if curr[j] == s2[i] and curr[j] != s2[j]:
                    nxt = list(curr)
                    nxt[i], nxt[j] = nxt[j], nxt[i]
                    nxt = ''.join(nxt)
                    if nxt not in visited:
                        visited.add(nxt)
                        queue.append((nxt, swaps + 1))

        return -1