class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)   # sentinel handles edge case: deleting head
        fast = dummy
        slow = dummy

        # Advance fast n+1 steps so the gap between fast and slow is exactly n
        for _ in range(n + 1):
            fast = fast.next

        # Move both until fast falls off the end
        while fast:
            fast = fast.next
            slow = slow.next

        # slow is now just before the target node
        slow.next = slow.next.next

        return dummy.next