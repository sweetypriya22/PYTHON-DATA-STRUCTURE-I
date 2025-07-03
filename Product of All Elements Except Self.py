'''
Write a function that takes a list of integers and returns a new list such that each element at index 'i' of the new list is the product of all the elements in the original list except the one at 'i'.

Avoid using division to handle cases involving zeros.
If the list contains only one element, return [1].


Input Format:

An integer 'n', the number of elements in the list.
A list of 'n' integers.
'''
from ast import literal_eval

# Input lena
n = int(input())
lst = literal_eval(input())

def product_except_self(lst):
    if len(lst) == 1:
        return [1]

    length = len(lst)
    left = [1] * length
    right = [1] * length
    output = [1] * length

    # Left product fill karo
    for i in range(1, length):
        left[i] = left[i - 1] * lst[i - 1]

    # Right product fill karo
    for i in range(length - 2, -1, -1):
        right[i] = right[i + 1] * lst[i + 1]

    # Final output banao
    for i in range(length):
        output[i] = left[i] * right[i]

    return output

# Print result
print(product_except_self(lst))

