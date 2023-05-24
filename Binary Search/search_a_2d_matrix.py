class Solution:
    def __init__(self):
        self.target = None
        self.matrix = None

    def searchMatrix(self, matrix, target: int) -> bool:
        self.target = target
        self.matrix = matrix

        row = self.findRow()
        if row == -1:
            return False
        result = self.binarySearch(self.matrix[row])
        return result


    def binarySearch(self, arr):
        l = 0
        r = len(arr) - 1

        while l <= r:
            m = (l + r) //2
            if self.target < arr[m]:
                r = m-1
            elif self.target > arr[m]:
                l = m+1
            else:
                return True
        return False


    def findRow(self):
        for i in range(len(self.matrix)):
            if self.target >= self.matrix[i][0] and self.target <= self.matrix[i][-1]:
                return i
        return -1


obj = Solution()
print(obj.searchMatrix(matrix = [[1,3]], target = 3))