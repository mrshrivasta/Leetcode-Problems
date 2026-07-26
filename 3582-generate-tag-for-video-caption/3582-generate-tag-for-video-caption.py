class Solution:
    def generateTag(self, caption: str) -> str:
        words = caption.split()
        if not words:
            return "#"
        result = words[0].lower() + ''.join(w.capitalize() for w in words[1:])
        return ('#' + result)[:100]