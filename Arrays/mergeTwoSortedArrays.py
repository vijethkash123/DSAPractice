class Solution:
    def merge(self, A, m, B, n):
        a, b, write_index = m-1, n-1, m + n - 1

        while b >= 0:
            if a >= 0 and A[a] > B[b]:
                A[write_index] = A[a]
                a -= 1
            else:
                A[write_index] = B[b]
                b -= 1

            write_index -= 1


obj = Solution()
obj.merge(A = [2,2,3,0,0,0], m = 3, B = [1,5,6], n = 3)