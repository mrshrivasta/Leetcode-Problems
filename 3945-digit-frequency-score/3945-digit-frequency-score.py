class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        freq = {}
        
        for ch in str(n):
            digit = int(ch)
            freq[digit] = freq.get(digit, 0) + 1
        
        score = 0
        for digit, count in freq.items():
            score += digit * count
        
        return score