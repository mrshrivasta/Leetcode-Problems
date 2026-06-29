class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching = {')': '(', ']': '[', '}': '{'}

        for char in s:
            if char in matching:                      # closing bracket
                top = stack.pop() if stack else None
                if top != matching[char]:
                    return False
            else:
                stack.append(char)                    # opening bracket

        return len(stack) == 0  # valid only if nothing is left unmatched