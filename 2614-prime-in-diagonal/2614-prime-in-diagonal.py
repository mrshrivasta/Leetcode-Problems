class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        def isPrime(n):
            if n < 2: return False
            if n < 4: return True
            if n % 2 == 0 or n % 3 == 0: return False
            for i in range(5, int(n**0.5)+1, 6):
                if n % i == 0 or n % (i+2) == 0: return False
            return True
        
        n, res = len(nums), 0
        for i in range(n):
            for val in {nums[i][i], nums[i][n-i-1]}:
                if isPrime(val): res = max(res, val)
        return res