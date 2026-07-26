from collections import Counter

class Solution:
    def originalDigits(self, s: str) -> str:
        cnt = Counter(s)
        num = [0] * 10

        num[0] = cnt['z']
        num[2] = cnt['w']
        num[4] = cnt['u']
        num[6] = cnt['x']
        num[8] = cnt['g']

        num[3] = cnt['h'] - num[8]
        num[5] = cnt['f'] - num[4]
        num[7] = cnt['s'] - num[6]

        num[1] = cnt['o'] - num[0] - num[2] - num[4]
        num[9] = cnt['i'] - num[5] - num[6] - num[8]

        return ''.join(str(i) * num[i] for i in range(10))