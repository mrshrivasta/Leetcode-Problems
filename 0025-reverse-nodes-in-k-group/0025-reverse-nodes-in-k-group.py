class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            # Step 1: check if k nodes remain
            kth = self.getKth(group_prev, k)
            if not kth:
                break

            group_next = kth.next  # save node after the group

            # Step 2: reverse k nodes
            prev, curr = kth.next, group_prev.next
            while curr != group_next:
                nxt        = curr.next
                curr.next  = prev
                prev       = curr
                curr       = nxt

            # Step 3: reconnect group to the main list
            connector      = group_prev.next  # will become the group's tail after reversal
            group_prev.next = kth             # kth is now the group's head after reversal
            group_prev      = connector       # advance prev to the group's tail

        return dummy.next

    def getKth(self, node: ListNode, k: int) -> Optional[ListNode]:
        while node and k > 0:
            node = node.next
            k -= 1
        return node