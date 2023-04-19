# For leetcode problem - https://leetcode.com/problems/minimum-additions-to-make-valid-string/

'''
Explanation from one of leetcode solutions:
We will do Circular Matching with abc, using which we will get to know the absent characters.

Explanation:
We will iterate and match with curr :
If matched, we will move forward
else, we will keep moving the curr only until it matches with current character.
Number of times curr mismatched is our answer

C++ code
int addMinimum(string A, char curr = 'a', int res = 0) {
    for(int i = 0;i < A.size();){
        if(A[i] == curr) ++i;
        else ++res;
		curr = 'a' + ((curr - 'a') + 1) % 3;
	}
    return res + (curr == 'a' ? 0 : 'c' - curr + 1);
}

'''

class Solution:
    def addMinimum(self, A, curr='a', res=0):
        for i in range(len(A)):
            if A[i] == curr:
                i += 1
            else:
                res += 1
            curr = chr(ord('a') + (ord(curr) - ord('a') + 1) % 3)
        return res + (0 if curr == 'a' else ord('c') - ord(curr) + 1)


obj = Solution()
print(obj.addMinimum("aabc"))

