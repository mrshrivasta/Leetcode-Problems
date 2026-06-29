class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]   # base sentinel: index before any valid substring
        max_len = 0

        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)    # push open bracket index
            else:
                stack.pop()        # try to match with top

                if not stack:
                    # No match available — this ')' is the new base
                    stack.append(i)
                else:
                    # Valid span from stack[-1]+1 to i (inclusive)
                    max_len = max(max_len, i - stack[-1])

        return max_len