class Solution:
    def averageWaitingTime(self, customers):
        cur = 0
        total = 0

        for a, t in customers:
            if cur < a:
                cur = a
            cur += t
            total += cur - a

        return total / len(customers)