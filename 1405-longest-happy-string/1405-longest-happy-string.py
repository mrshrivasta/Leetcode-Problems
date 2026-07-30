class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        result = []
        # Max heap: store (-count, char)
        heap = [(-cnt, ch) for cnt, ch in [(a,'a'),(b,'b'),(c,'c')] if cnt > 0]
        heapq.heapify(heap)

        while heap:
            cnt1, ch1 = heapq.heappop(heap)

            # Check if we'd create triple — if last two chars are same as ch1
            if len(result) >= 2 and result[-1] == ch1 and result[-2] == ch1:
                if not heap:
                    break
                cnt2, ch2 = heapq.heappop(heap)
                result.append(ch2)
                cnt2 += 1  # increment since counts are negative
                if cnt2 < 0:
                    heapq.heappush(heap, (cnt2, ch2))
                heapq.heappush(heap, (cnt1, ch1))
            else:
                result.append(ch1)
                cnt1 += 1  # increment since counts are negative
                if cnt1 < 0:
                    heapq.heappush(heap, (cnt1, ch1))

        return ''.join(result)