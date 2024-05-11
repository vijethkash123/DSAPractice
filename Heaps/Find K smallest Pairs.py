import heapq
from typing import Optional, List

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        res = []
        visited = set()
        heap = [(nums1[0] + nums2[0], 0, 0)]  # aadding the first element
        visited.add((0, 0))
        # Heap structure -> (sum, i, j)v -> i to iterate over nums1 and j to iterate over nums2
        heapq.heapify(heap)
        while heap and len(res) < k:
            _, i, j = heapq.heappop(heap)
            res.append([nums1[i], nums2[j]])

            if i+1 < len(nums1) and (i + 1, j) not in visited:
                heapq.heappush(heap, (nums1[i + 1] + nums2[j], i + 1, j))
                visited.add((i + 1, j))

            if j+1 < len(nums2) and (i, j + 1) not in visited:
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
                visited.add((i, j + 1))
        
        return res


print(Solution().kSmallestPairs([1,2,4,5,6], [3,5,7,9], 20))
# res = [[1,3],[2,3],[1,5],[2,5],[4,3],[1,7],[5,3],[2,7],[4,5],[6,3],[1,9], [5,5],[2,9],[4,7],[6,5],[5,7],[4,9],[6,7],[5,9],[6,9]]

