'''
Write a program that takes two strings, 'a' and 'b', as input and merges them by alternating characters from both strings.



The program's task is to construct and return a new string formed by alternating characters from each string.

Start by taking one character from string 'a', then one from string 'b', and continue this pattern.
If one string runs out of characters before the other, append the remaining part of the longer string to the result.
'''
# Taking input
a = input()
b = input()

def merge_alternate(a, b):
    result = []
    for i in range(max(len(a), len(b))):
        if i < len(a):
            result.append(a[i])
        if i < len(b):
            result.append(b[i])
    return "".join(result)

print(merge_alternate(a, b))