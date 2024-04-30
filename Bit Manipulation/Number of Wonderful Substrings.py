# class Solution(object):
#     def wonderfulSubstrings(self, word):
#         count = [0] * 1024  # 2^10 to store XOR values
#         result = 0
#         prefix_xor = 0
#         count[prefix_xor] = 1
#         cc = 0
#         for char in word:
#             char_index = ord(char) - ord('a')
#             # print(char_index, 1 << char_index)
#             prefix_xor ^= 1 << char_index
#             print("PERFIX XOR")
#             print(prefix_xor)
#             print("CC")
#             cc = cc ^ char_index + 1
#             print(cc)



class Solution(object):
    def wonderfulSubstrings(self, word):
        count = [0] * 1024  # 2^10 to store XOR values
        result = 0
        prefix_xor = 0
        count[prefix_xor] = 1
        
        for char in word:
            char_index = ord(char) - ord('a')
            prefix_xor ^= 1 << char_index
            result += count[prefix_xor]  # even case, same prefix occuredd before, if so how many times? add number of times, same as subarray sum equals k concept
            for i in range(10):
                print(prefix_xor ^ (1 << i))
                result += count[prefix_xor ^ (1 << i)]  # odd case, standing at current character, checking till what all indexes that character occurs odd number of times.
            count[prefix_xor] += 1
        
        return result

print(Solution().wonderfulSubstrings("aab"))


# 1 << char_index  --> means left shift 1 by char_index bits
# Ex: char index will be 1 for b
# 1 << 1 -> 10 -> 2
# equivalent to saying a is 0000000001, b is 0000000010, c is 0000000100

