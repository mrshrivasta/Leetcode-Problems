from collections import deque

class Solution:
    def longestSubarray(self, nums, limit):
        maxdq = deque()
        mindq = deque()
        left = 0
        ans = 0

        for right, x in enumerate(nums):
            while maxdq and maxdq[-1] < x:
                maxdq.pop()
            maxdq.append(x)

            while mindq and mindq[-1] > x:
                mindq.pop()
            mindq.append(x)

            while maxdq[0] - mindq[0] > limit:
                if nums[left] == maxdq[0]:
                    maxdq.popleft()
                if nums[left] == mindq[0]:
                    mindq.popleft()
                left += 1

            ans = max(ans, right - left + 1)

        return ans