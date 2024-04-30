
masked = {chr(val): val-96 for val in range(ord('a'), ord('j')+1)}
print(masked)

word = "aab"
prefixXor = [0] * 4
xorred = 0
for i, c in enumerate(word):
    xorred = xorred ^ masked[c]
    prefixXor[i+1] = xorred

print(prefixXor)


# LeetCode 1915
class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        ans = 0
        # creating respective masks from A to J
        masked = {chr(val): val-96 for val in range(ord('a'), ord('j')+1)}

        for j in range(len(word)):
            xorred = 0
            prefixXor = [0] * (len(word[j:]) + 1)
            for i, c in enumerate(word[j:]):
                print(word[j:])
                xorred = xorred ^ masked[c]
                if xorred in prefixXor:
                    ans += 1
                prefixXor[i+1] = xorred
            
        return ans



# print(Solution().wonderfulSubstrings("aabb"))
print(Solution().wonderfulSubstrings("aab"))
