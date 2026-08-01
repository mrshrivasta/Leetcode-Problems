class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counts = defaultdict(int)

        for entry in cpdomains:
            rep, domain = entry.split()
            rep = int(rep)
            parts = domain.split('.')
            for i in range(len(parts)):
                counts['.'.join(parts[i:])] += rep

        return [f"{v} {k}" for k, v in counts.items()]