from heapq import heappush, heappop

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        heap = []

        # Seed the heap with the head of each non-empty list
        # Tie-break with index i to avoid comparing ListNodes directly
        for i, node in enumerate(lists):
            if node:
                heappush(heap, (node.val, i, node))

        while heap:
            val, i, node = heappop(heap)
            current.next = node
            current = current.next

            if node.next:
                heappush(heap, (node.next.val, i, node.next))

        return dummy.next