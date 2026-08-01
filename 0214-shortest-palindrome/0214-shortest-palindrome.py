class Solution:
    def shortestPalindrome(self, s: str) -> str:
        # KMP failure function on s + '#' + reversed(s)
        # to find longest palindromic prefix of s
        t = s + "#" + s[::-1]
        n = len(t)

        fail = [0] * n
        j = 0
        for i in range(1, n):
            while j > 0 and t[i] != t[j]:
                j = fail[j - 1]
            if t[i] == t[j]:
                j += 1
            fail[i] = j

        longest_palindrome_prefix = fail[-1]
        suffix_to_add = s[longest_palindrome_prefix:][::-1]
        return suffix_to_add + s