class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        h = [-x for x in gifts]
        heapq.heapify(h)
        for _ in range(k):
            heapq.heapreplace(h, -int((-h[0]) ** 0.5))
        return -sum(h)