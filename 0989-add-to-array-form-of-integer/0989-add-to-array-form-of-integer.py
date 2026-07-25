class Solution:
    def addToArrayForm(self, num, k):
        carry = k
        for i in range(len(num) - 1, -1, -1):
            carry += num[i]
            num[i] = carry % 10
            carry //= 10
        while carry:
            num.insert(0, carry % 10)
            carry //= 10
        return num