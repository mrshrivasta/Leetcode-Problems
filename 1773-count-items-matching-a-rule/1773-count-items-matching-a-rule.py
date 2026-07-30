class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        idx = {"type": 0, "color": 1, "name": 2}[ruleKey]
        return sum(item[idx] == ruleValue for item in items)