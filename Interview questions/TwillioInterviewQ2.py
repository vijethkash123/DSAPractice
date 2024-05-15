def minSwaps(s: str) -> int:
    xlist = [i for i in s]
    end = len(s) - 1
    stack = 0
    ans = 0

    oc, cc = 0, 0
    for i in s:
        if i == "[":
            oc+=1
        else:
            cc+=1
    if oc != cc:
        return -1



    for start in range(end):
        if s[start] == '[':
            stack += 1
        elif stack:
            stack -= 1
        else:
            ans += 1

            while s[end] != '[':
                end -= 1
            xlist[start], xlist[end] = xlist[end], xlist[start]  # added for debugging how the output after the swaps will look it
            stack += 1
            end -= 1
    
    print(''.join(xlist))
    return ans

# Example usage
brackets = "]]][[[[]"
result = minSwaps(brackets)
print(result)  # Output: 2
# After balancing: [][[[]]]
print(minSwaps("]][]]"))  # -1
