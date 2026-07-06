class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        i = 0
        while i < len(data):
            b = data[i]
            if b >> 7 == 0: n = 1
            elif b >> 5 == 0b110: n = 2
            elif b >> 4 == 0b1110: n = 3
            elif b >> 3 == 0b11110: n = 4
            else: return False
            for j in range(i+1, i+n):
                if j >= len(data) or data[j] >> 6 != 0b10: return False
            i += n
        return True