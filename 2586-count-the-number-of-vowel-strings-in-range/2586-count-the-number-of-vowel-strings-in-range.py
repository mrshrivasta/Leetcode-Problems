class Solution:
    def vowelStrings(self, words: list[str], left: int, right: int) -> int:
        v = set('aeiou')
        return sum(1 for w in words[left:right+1] if w[0] in v and w[-1] in v)