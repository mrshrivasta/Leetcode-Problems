class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        n = len(num)

        def backtrack(index, seq):
            if index == n and len(seq) >= 3:
                return seq

            for end in range(index + 1, n + 1):
                part = num[index:end]

                # No leading zeros (except "0" itself)
                if len(part) > 1 and part[0] == '0':
                    break

                val = int(part)

                # 32-bit signed integer check
                if val > 2**31 - 1:
                    break

                if len(seq) >= 2 and val != seq[-1] + seq[-2]:
                    # If val is too small, keep extending; if too large, stop
                    if val < seq[-1] + seq[-2]:
                        continue
                    else:
                        break

                result = backtrack(end, seq + [val])
                if result:
                    return result

            return []

        return backtrack(0, [])