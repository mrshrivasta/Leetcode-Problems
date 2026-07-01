from collections import deque

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank = set(bank)

        if endGene not in bank:
            return -1

        q = deque([(startGene, 0)])
        visited = {startGene}
        genes = "ACGT"

        while q:
            gene, steps = q.popleft()

            if gene == endGene:
                return steps

            for i in range(8):
                for ch in genes:
                    mutated = gene[:i] + ch + gene[i + 1:]

                    if mutated in bank and mutated not in visited:
                        visited.add(mutated)
                        q.append((mutated, steps + 1))

        return -1