class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        diffs = [(a, b) for a, b in zip(s, goal) if a != b]

        if len(diffs) == 0:
            # Need a duplicate char in s to swap with itself
            return len(set(s)) < len(s)
        if len(diffs) == 2:
            return diffs[0] == diffs[1][::-1]
        return False