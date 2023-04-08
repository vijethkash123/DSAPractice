class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points:
            return 0

        points.sort()
        # print(points) 
        result = 0
        i = 0
        while i < len(points):
            j = i + 1
            right_bound = points[i][1]
            while j < len(points) and points[j][0] <= right_bound:
                right_bound = min(right_bound, points[j][1])
                j += 1
            result += 1
            i = j
        return result

if __name__ == "__main__":
    obj=Solution()
    print(obj.findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]))
    print(obj.findMinArrowShots([[1,2],[3,4],[5,6],[7,8]]))
