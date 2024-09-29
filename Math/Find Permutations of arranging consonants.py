# import math

"""
You are given a string S and your task is to find and 
return the count of permutations formed by fixing the positions of the vowels present in the string.
Note:
Ensure the result is non-negative.
If there are no consonents then return 0.

Solution:
We fix the positions of vowels. and we have spaces for consonants. _ _ _
Now we have to find different ways of filling these gaps with consonants
It's just the factorial of consonants count, we don't care about vowels as it's fixed in it's positions and we can move around consonants
"""
def count_vowel_permutations(s):
    vowel_count = 0
    consonant_count = 0

    for char in s:
        if char.lower() in "aeiou":
            vowel_count += 1
        else:
            consonant_count += 1

    if consonant_count == 0:
        return 0

    permutations = 1
    for i in range(1, consonant_count + 1):
        permutations *= i

    return permutations

# Example usage:
string = "ABCDE"
result = count_vowel_permutations(string)
print("Number of permutations:", result)

# print(math.perm(3, 3))