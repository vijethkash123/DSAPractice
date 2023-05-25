class Solution:
    def minDays(self, bloomDay, m: int, k: int) -> int:
        res = float("inf")

        got_ans = False
        temp_m = m
        count = 0
        if m*k > len(bloomDay): 
            # if number of boquets * number of adjacent flowers should always be lesser than number of elements in the bloomDay array, otherwise we cannot get k adjascent flowers to fill m boquets
            return -1
        l = 1 # Minimum number of days any flower can take to bloom
        r = max(bloomDay) # Because, it's the maximum number days any flower can take to bloom

        while l<=r:
            got_ans = False
            temp_m = m
            count = 0

            mid = (l+r)//2 # mid is the number of days 

            for i in bloomDay:
                if i<=mid: # We check if each flower can bloom in `mid` days
                    count += 1 
                else:
                    count = 0 # if not adjascent break the counter
                if count == k: 
                    count = 0
                    temp_m -= 1 # to check if boquets are filled
                if temp_m == 0:
                    res = min(res,mid)
                    got_ans = True
                    break
            
            if got_ans == True: # checking if we got a `mid` value in which k adjascent flowers can bloom to fill in m boquets
                r = mid - 1 # We do this, because we want to return the minimum number of days required to fill m boquets with k adjacent flowers.
            else:
                l = mid + 1

        return res

obj = Solution()
print(obj.minDays(bloomDay = [1,10,3,10,2], m = 3, k = 1))