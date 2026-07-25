class Solution:
    def flipAndInvertImage(self, image):
        return [[1 ^ x for x in row[::-1]] for row in image]