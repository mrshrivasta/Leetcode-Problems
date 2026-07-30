class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        index = {v: i for i, v in enumerate(list1)}
        min_sum = float('inf')
        result = []
        for j, v in enumerate(list2):
            if v in index:
                s = index[v] + j
                if s < min_sum:
                    min_sum = s
                    result = [v]
                elif s == min_sum:
                    result.append(v)
        return result