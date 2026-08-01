class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = list(map(int, version1.split('.')))
        v2 = list(map(int, version2.split('.')))

        length = max(len(v1), len(v2))
        v1 += [0] * (length - len(v1))
        v2 += [0] * (length - len(v2))

        for a, b in zip(v1, v2):
            if a < b: return -1
            if a > b: return  1
        return 0