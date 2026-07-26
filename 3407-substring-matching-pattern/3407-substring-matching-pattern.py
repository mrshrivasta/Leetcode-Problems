class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        left, right = p.split('*')
        for i in range(len(s)):
            if s[i:i+len(left)] == left:
                rest = s[i+len(left):]
                if right in rest or right == '':
                    if rest.find(right) != -1 or right == '':
                        return True
        return False