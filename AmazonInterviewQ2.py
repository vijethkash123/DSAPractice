'''
Your team at Amazon is working on a system that divides applications to a mixed cluster of computing devices. Each application is identified by an integer ID, requires a fixed non-zero amount of memory to execute, and is defined to be either a foreground or background application. IDs are guaranteed to be unique within their own application type, but not across types.
Each device should be assigned two applications at once, one foreground application and one background application. Devices have limited amounts of memory and cannot execute applications that require more memory than the available memory. The goal of the system is to maximize the total utilization of the memory of a given device. A foreground/background application pair is considered to be optimal if there does not exist another pair that uses more memory than this pair, and also has a total less than or equal to the total memory of the device. For example, if the device has 10MB memory, a foreground/background pair using a sum total of 9MB memory would be optimal if there does not exist a pair that uses a sum total of 10 MB, but would not be optimal if such a pair did exist.
Write an algorithm to find the sets of foreground and background application pairs that optimally utilize the given device for a given list of foreground applications and a given list of background applications.

Input
The input to the function/method consists of three arguments: deviceCapacity, an integer representing the maximum capacity of the given device; foregroundAppList, a list of pairs of integers where the first integer represents the unique ID of a foreground application and the second integer represents the amount of memory required by this application;
backgroundAppList, a list of pairs of integers where the first integer represents the unique ID of a background application and the second integer represents the amount of memory required by this application.

Output
Return a list of pairs of integers representing the pairs of IDs of foreground and background applications that optimally utilize the given device [foregroundApp|D, backgroundAppID]. If no pair is possible, return a list with empty pair - not just an empty list.

Example 1:
Input:
deviceCapacity = 7
foregroundAppList = [[1,2],[2,4],[3,6]]
backgroundApplist = [1,2]
Output:
[2,1]
Explanation:
There are only three combinations, [1,1], [2,1], and [3,1], Which use a total of 4, 6, and 8 MB memory, respectively. Since 6 is the largest use that does not exceed 7, [2,1] is the only optimal pair.
'''

from collections import defaultdict
def getOptimalPairs(deviceCapacity, foregroundAppList, backgroundAppList):
    # Initialize variables to keep track of the best pair and the maximum memory usage
    bestPair = defaultdict(list)
    maxMemory = 0
    # Loop through the foreground and background lists
    for i in range(len(foregroundAppList)):
        for j in range(len(backgroundAppList)):
            # Check if the sum of the memory usage is within the device capacity
            memoryUsage = foregroundAppList[i][1] + backgroundAppList[j][1]
            if memoryUsage <= deviceCapacity:
                # If the memory usage is higher than the current best, update the best pair and the maximum memory usage
                if memoryUsage >= maxMemory:
                    bestPair[memoryUsage].append([foregroundAppList[i][0], backgroundAppList[j][0]])
                    maxMemory = memoryUsage
    # Return the best pair, or an empty pair if no pair was found
    maxMemFound = max(bestPair.keys()) if bestPair else None
    return bestPair[maxMemFound] if bestPair else [()]

print(getOptimalPairs(7,[[1,2],[2,4],[3,6]], [[1,2]]))
print(getOptimalPairs(10, [[1,3],[2,5],[3,7],[4,10]], [[1,2],[2,3],[3,4],[4,5]]))
print(getOptimalPairs(16,[[2,7],[3,14]], [[2,10],[3,14]]))