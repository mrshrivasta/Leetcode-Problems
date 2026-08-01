class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []
        
        while columnNumber > 0:
            columnNumber -= 1  # Adjust to 0-indexed (A=0, B=1, ..., Z=25)
            result.append(chr(columnNumber % 26 + ord('A')))
            columnNumber //= 26
        
        return "".join(reversed(result))