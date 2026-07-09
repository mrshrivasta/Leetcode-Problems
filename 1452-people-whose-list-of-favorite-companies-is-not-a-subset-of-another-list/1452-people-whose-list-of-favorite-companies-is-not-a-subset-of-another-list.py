from typing import List

class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        sets = [set(companies) for companies in favoriteCompanies]
        ans = []

        for i in range(len(sets)):
            is_subset = False

            for j in range(len(sets)):
                if i == j:
                    continue

                if len(sets[i]) > len(sets[j]):
                    continue

                if sets[i].issubset(sets[j]):
                    is_subset = True
                    break

            if not is_subset:
                ans.append(i)

        return ans