class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        def isPrime(n):
            if n < 2: return False
            return all(n % i for i in range(2, int(n**0.5)+1))
        return any(isPrime(v) for v in Counter(nums).values())