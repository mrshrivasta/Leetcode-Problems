class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        def height(a, b):
            h = 0
            for i in range(1, 201):
                if i % 2 == 1:
                    if a >= i: a -= i
                    else: break
                else:
                    if b >= i: b -= i
                    else: break
                h += 1
            return h
        return max(height(red, blue), height(blue, red))