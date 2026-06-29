class Solution:
    def countAndSay(self, n: int) -> str:
        current = "1"

        for _ in range(n - 1):
            next_term = []
            i = 0

            while i < len(current):
                char  = current[i]
                count = 1

                while i + count < len(current) and current[i + count] == char:
                    count += 1

                next_term.append(str(count))
                next_term.append(char)
                i += count   # jump past the entire run

            current = "".join(next_term)

        return current