from collections import Counter, defaultdict

class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        count = Counter(s)
        groups = defaultdict(list)
        for c, f in count.items():
            groups[f].append(c)
        best_k = max(groups, key=lambda k: (len(groups[k]), k))
        return ''.join(groups[best_k])