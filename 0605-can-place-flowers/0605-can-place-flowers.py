class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                prev = (i == 0) or (flowerbed[i-1] == 0)
                next = (i == len(flowerbed)-1) or (flowerbed[i+1] == 0)
                if prev and next:
                    flowerbed[i] = 1
                    n -= 1
        return n <= 0