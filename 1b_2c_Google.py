# n is total number of characters. 
# bCount and cCount are counts 
# of 'b' and 'c' respectively.
def countStr(n, bCount, cCount): 

	# Base cases 
	if (bCount < 0 or cCount < 0): 
		return 0
	if (n == 0) : 
		return 1
	if (bCount == 0 and cCount == 0): 
		return 1

	# Three cases, we choose, a or b or c 
	# In all three cases n decreases by 1. 
	res = countStr(n - 1, bCount, cCount) 
	res += countStr(n - 1, bCount - 1, cCount) 
	res += countStr(n - 1, bCount, cCount - 1) 

	return res 

# Driver code 
if __name__ =="__main__": 
	n = 3 # Total number of characters 
	print(countStr(n, 1, 2)) 

# This code is contributed 
# by ChitraNayal 
