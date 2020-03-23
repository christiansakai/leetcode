import heapq
from typing import List

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counts = {}
        for word in words:
            if word not in counts:
                counts[word] = 1
            else:
                counts[word] += 1

        heap = []
        for word in counts:
            heapq.heappush(heap, (counts[word] * -1, word))

        result = []
        for i in range(k):
            result.append(heapq.heappop(heap)[1])

        return result
