class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        answer = [n] * n

        # Left pass: propagate distances from left occurrences of c
        prev = -n
        for i in range(n):
            if s[i] == c:
                prev = i
            answer[i] = i - prev

        # Right pass: propagate distances from right occurrences of c
        prev = 2 * n
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                prev = i
            answer[i] = min(answer[i], prev - i)

        return answer