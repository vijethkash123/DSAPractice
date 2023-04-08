maxint=99999
def maxSubArraySum(a,size): 
       
    max_so_far = -maxint - 1
    print("--------------")
    print(max_so_far)
    
    max_ending_here = 0
       
    for i in range(0, size): 
        max_ending_here = max_ending_here + a[i] 
        if (max_so_far < max_ending_here): 
            max_so_far = max_ending_here 
  
        if max_ending_here < 0: 
            max_ending_here = 0   
        print(max_so_far,max_ending_here)
    return max_so_far 
if __name__ =='__main__':
    a = [-2,-1,-7,-4]
    print ("Maximum contiguous sum is "+ str(maxSubArraySum(a,len(a))))