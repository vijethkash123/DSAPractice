'''
We sort the array in O(n.log(n)) time complexity.
We have this complexity because, we divide the input array into 2 halves in each step. 
This means log to base 2,
which is division of input into half, 
so if input array is of size 6, we have 3 steps in total.
And even though left completes recursive branching to meet base case first and then right is called, it is
log(n) because it is divided into left and right arrays in each 'pass'/ function call.
and the overall complexity is O(n.log(n)) because for each sub array, we sort n elements in each pass.
'''

class Sort:
    def mergeSort(self, arr: list):
        if len(arr) in (1,0):   # Base cases
            return arr

        mid = len(arr)//2  # Calcualte mid
        
        left = self.mergeSort(arr[:mid])  # Recursive call to split untill base case is met
        right = self.mergeSort(arr[mid:])
        
        return self.merge(left, right)

    def merge(self, left, right):
        ans = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                ans.append(left[i])
                i+=1
            else:
                ans.append(right[j])
                j+=1

        while i < len(left):
            ans.append(left[i])
            i+=1
        while j < len(right):
            ans.append(right[j])
            j+=1
        return ans

obj = Sort()
print(obj.mergeSort([6,5,4,3,2,1]))
print(obj.mergeSort([]))
print(obj.mergeSort([1,2,2,1,1]))
