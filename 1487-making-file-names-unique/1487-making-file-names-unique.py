from typing import List

class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        used = {}
        ans = []

        for name in names:
            if name not in used:
                ans.append(name)
                used[name] = 1
            else:
                k = used[name]

                while f"{name}({k})" in used:
                    k += 1

                new_name = f"{name}({k})"

                ans.append(new_name)

                used[name] = k + 1
                used[new_name] = 1

        return ans