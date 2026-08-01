class Solution:
    def uniqueLetterString(self, s: str) -> int:
        # For each char, track last two positions seen
        last = defaultdict(lambda: [-1, -1])
        result = 0

        for i, c in enumerate(s):
            prev2, prev1 = last[c]
            # Contribution of s[i] as a unique char:
            # left choices:  i - prev1 (indices from prev1+1 to i)
            # right choices: prev1 - prev2 ... wait, need right boundary too
            # Actually we compute contribution when we see the NEXT occurrence
            # So track and finalize at each step:
            result += (i - prev1) * (prev1 - prev2)
            last[c] = [prev1, i]

        # Finalize remaining characters (treat end of string as next occurrence)
        n = len(s)
        for c, (prev2, prev1) in last.items():
            if prev1 != -1:
                result += (n - prev1) * (prev1 - prev2)

        return result