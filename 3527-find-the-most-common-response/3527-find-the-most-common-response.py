class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        count = Counter(word for day in responses for word in set(day))
        return min(count, key=lambda w: (-count[w], w))