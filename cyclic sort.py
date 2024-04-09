# Function to sort the array 
def sort(arr, n): 
	i = 0
	while(i < n): 
		# finding the correct index 
		correct = arr[i]-1

		# Element index and value not match 
		# then swapping 
		if arr[correct] != arr[i]: 
			# calling swap function 
			swap(arr, i, correct) 
		else:   # We keep swapping untill the index comes to right position in each iteration.
			i = i + 1

# function to swap values 
def swap(arr, first, second): 
	temp = arr[first] 
	arr[first] = arr[second] 
	arr[second] = temp 

# Driver Code 
# arr = [3, 2, 5, 6, 1, 4] 
arr = [5,4,1,2,3]
n = len(arr) 

# function call 
sort(arr, n) 

# printing the answer 
for i in range(0, n): 
	print(arr[i], end=" ") 

# This code is contributed by Yash Agarwal(yashagarwal2852002) 
