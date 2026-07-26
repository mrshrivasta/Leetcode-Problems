from collections import defaultdict

class Solution:
    def displayTable(self, orders):
        foods = sorted({food for _, _, food in orders})
        tables = defaultdict(lambda: defaultdict(int))

        for _, table, food in orders:
            tables[int(table)][food] += 1

        ans = [["Table"] + foods]

        for table in sorted(tables):
            row = [str(table)]
            for food in foods:
                row.append(str(tables[table][food]))
            ans.append(row)

        return ans