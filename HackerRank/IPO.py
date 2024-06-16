# MinHeap + MaxHeap -> Two Heap pattern
import heapq
from typing import List


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        maxProfit = []  # maxHeap
        minCapital = [(c, p)for c, p in zip(capital, profits)]  # minHeap

        heapq.heapify(minCapital)
        for _ in range(k):
            while minCapital and minCapital[0][0] <= w:
                c, p = heapq.heappop(minCapital)
                heapq.heappush(maxProfit, -p)  # -p because maxHeap
            if not maxProfit:
                break
            w += abs(heapq.heappop(maxProfit))  # pops only k times

        return w


print(Solution().findMaximizedCapital(k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]))