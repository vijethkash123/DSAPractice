def searchMin(nums, target: int) -> int: #MIN
   left, right = 0, len(nums)-1
   while left < right:
       mid = left + (right-left)//2
       if nums[mid] >= target:
           right = mid
       else:
           left = mid+1
   return right 

print(searchMin([1,2,3,3,4,5,6], 3.5))
