class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        lines, current, length = [], [], 0

        for word in words:
            if length + len(word) + len(current) > maxWidth:
                lines.append(current)
                current, length = [], 0
            current.append(word)
            length += len(word)
        lines.append(current)

        result = []
        for i, line in enumerate(lines):
            if i == len(lines) - 1 or len(line) == 1:
                result.append(" ".join(line).ljust(maxWidth))
                continue
            spaces = maxWidth - sum(len(w) for w in line)
            gaps = len(line) - 1
            even, extra = divmod(spaces, gaps)
            row = ""
            for j, word in enumerate(line[:-1]):
                row += word + " " * (even + (1 if j < extra else 0))
            result.append(row + line[-1])

        return result