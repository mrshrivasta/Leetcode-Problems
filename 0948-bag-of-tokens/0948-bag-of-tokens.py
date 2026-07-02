class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()

        left, right = 0, len(tokens) - 1
        score = 0
        ans = 0

        while left <= right:
            if power >= tokens[left]:
                power -= tokens[left]
                score += 1
                ans = max(ans, score)
                left += 1
            elif score > 0:
                power += tokens[right]
                score -= 1
                right -= 1
            else:
                break

        return ans