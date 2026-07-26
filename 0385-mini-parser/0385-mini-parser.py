class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        if s[0] != '[':
            return NestedInteger(int(s))

        stack = []
        num = ""
        
        for ch in s:
            if ch == '[':
                stack.append(NestedInteger())
            elif ch == '-' or ch.isdigit():
                num += ch
            elif ch in ',]':
                if num:
                    stack[-1].add(NestedInteger(int(num)))
                    num = ""
                
                if ch == ']' and len(stack) > 1:
                    ni = stack.pop()
                    stack[-1].add(ni)

        return stack[0]