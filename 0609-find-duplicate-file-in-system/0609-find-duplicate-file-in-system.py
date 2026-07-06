from typing import List
from collections import defaultdict

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_map = defaultdict(list)

        for path in paths:
            parts = path.split()
            directory = parts[0]

            for file_info in parts[1:]:
                name, content = file_info.split('(')
                content = content[:-1]  # remove ')'

                full_path = directory + '/' + name
                content_map[content].append(full_path)

        return [group for group in content_map.values() if len(group) > 1]