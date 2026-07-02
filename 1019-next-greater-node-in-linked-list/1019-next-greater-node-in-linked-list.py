# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def nextLargerNodes(self, head):
        nums = []

        while head:
            nums.append(head.val)
            head = head.next

        n = len(nums)
        ans = [0] * n
        stack = []  # stores indices

        for i in range(n):
            while stack and nums[i] > nums[stack[-1]]:
                idx = stack.pop()
                ans[idx] = nums[i]

            stack.append(i)

        return ans