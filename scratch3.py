class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        hamming_distance = 0
        new = x ^ y
        while new > 0:
            new = new & (new-1)
            hamming_distance += 1
        return hamming_distance
    
# print(Solution().hammingDistance(7, 0))

# 1001 - 9
# 1000 - 8
# 0111 - 7 
# 0110 - 6
# 0101 - 5
# 1011 - 11
# 1010 - 10

1111 - 15
1110 - 14
1101 - 13
1100 - 12
print(15 & 14)