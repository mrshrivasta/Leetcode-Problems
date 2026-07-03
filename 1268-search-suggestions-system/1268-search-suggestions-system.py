class Solution:
    def suggestedProducts(self, products, searchWord):
        products.sort()
        res = []
        prefix = ""

        for ch in searchWord:
            prefix += ch
            i = 0
            temp = []

            for p in products:
                if p.startswith(prefix):
                    temp.append(p)
                    if len(temp) == 3:
                        break

            res.append(temp)

        return res