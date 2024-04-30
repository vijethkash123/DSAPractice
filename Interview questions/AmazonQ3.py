'''
https://www.reddit.com/r/leetcode/comments/1bkyrej/completely_stumped_by_this_question/
'''
def solve(t):
    ans = 0
    delta = 0
    for n in reversed(t):
        ans += abs(-(n+delta))
        delta += -(n+delta)
    return ans

print(solve([2,-3,5]))  # 18
print(solve([-1,-1,-1,-1]))  # 1
