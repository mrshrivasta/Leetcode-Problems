class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []

        def backtrack(start: int, current: List[int], remaining: int) -> None:
            if remaining == 0:
                result.append(current[:])
                return

            for i in range(start, len(candidates)):
                if candidates[i] > remaining:
                    break                          # sorted → nothing ahead can help

                # Skip duplicates at the same depth level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                current.append(candidates[i])
                backtrack(i + 1, current, remaining - candidates[i])  # i+1: no reuse
                current.pop()

        backtrack(0, [], target)
        return result