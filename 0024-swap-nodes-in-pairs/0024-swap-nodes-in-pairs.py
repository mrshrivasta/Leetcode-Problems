class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy

        while prev.next and prev.next.next:
            first  = prev.next
            second = prev.next.next

            # Rewire
            prev.next   = second
            first.next  = second.next
            second.next = first

            # Advance prev to the last node of the swapped pair
            prev = first

        return dummy.next