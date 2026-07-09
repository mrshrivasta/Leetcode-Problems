class Solution:
    def buildArray(self, target, n):
        ans = []
        cur = 1

        for x in target:
            while cur < x:
                ans.append("Push")
                ans.append("Pop")
                cur += 1

            ans.append("Push")
            cur += 1

        return ans