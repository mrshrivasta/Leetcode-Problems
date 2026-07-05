# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import List, Optional

class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        nums_set = set(nums)
        count = 0

        while head:
            if head.val in nums_set and (
                head.next is None or head.next.val not in nums_set
            ):
                count += 1

            head = head.next

        return count