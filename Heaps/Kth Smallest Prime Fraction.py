import heapq
from typing import Optional, List


# Complexity is O(n^2 log n)	
# The nested loops iterate over the elements of the 'arr' list, resulting in O(n^2) iterations. Within the nested loops, heapq.heappush() is called, which has a time complexity of O(log n) where n is the number of elements in the heap. Therefore, the overall time complexity is O(n^2 log n).
class Solution:
    def kthSmallestPrimeFractionM1(self, arr: List[int], k: int) -> List[int]:
        heap = []
        heapq.heapify(heap)
        for i in range(len(arr)):
            for j in range(len(arr)):
                if arr[i] != arr[j]:
                    heapq.heappush(heap, (arr[i]/ arr[j], arr[i], arr[j]))

        n1, n2 = 0, 0
        i = 0
        while heap and i < k:
            _, n1, n2 = heapq.heappop(heap)
            i += 1
        
        return [n1, n2]


# Complexity (n+k * (logn))
    def kthSmallestPrimeFractionM2(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        heap = []
        heapq.heapify(heap)
        for i in range(n-1):
            heapq.heappush(heap, (arr[i]/ arr[-1], i, n-1, str(arr[i]) + "/" + str(arr[-1])))
        
        while k - 1 > 0:
            _, i, j, _ = heapq.heappop(heap)
            if i < j - 1:
                print(str(arr[i]) + "/" + str(arr[j-1]))
                heapq.heappush(heap, (arr[i]/ arr[j-1], i, j-1, str(arr[i]) + "/" + str(arr[j-1])))
            
            k -= 1
        return [arr[heap[0][1]], arr[heap[0][2]]]

# Using Binary Search: O(n * log(n)) approach
    def kthSmallestPrimeFractionM3(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        l, r = 0, 1   # because all the fractions are between 0 and 1
        p = q = 0
        while l < r:
            m = (l+r) / 2 # not floor division as we want decimals/ float

            maxFrac = 0
            cnt = 0
            j = 1
            for i in range(n-1):
                while j < n and arr[i] / arr[j] > m:
                    j += 1  # keep moving j forward in  the sorted list untill we find the first True value where arr[i]/arr[j] > m

                if j == n:
                    break
                
                # from the point j to rest of array, is the count of items that have fractions greater than k
                cnt += n-j  # the remaining part from j to n
                
                if arr[i]/ arr[j] > maxFrac:
                    p = arr[i]
                    q = arr[j]
                    maxFrac = p / q

            if cnt == k:
                return p, q
            elif cnt < k:
                l = m
            else:
                r = m


# print(Solution().kthSmallestPrimeFractionM3(arr = [1,2,3,5,7,11,13], k = 3))
print(Solution().kthSmallestPrimeFractionM3(arr = [1,2,3,5], k = 3))
