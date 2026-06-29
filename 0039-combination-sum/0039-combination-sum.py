class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(start: int, current: List[int], remaining: int) -> None:
            if remaining == 0:
                result.append(current[:])   # found valid combination
                return
            if remaining < 0:
                return                       # overshot — prune

            for i in range(start, len(candidates)):
                current.append(candidates[i])
                backtrack(i, current, remaining - candidates[i])  # i, not i+1 (reuse allowed)
                current.pop()

        backtrack(0, [], target)
        return result