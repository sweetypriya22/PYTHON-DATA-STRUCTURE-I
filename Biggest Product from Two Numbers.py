#Biggest Product from Two Numbers
'''
Write a function ‘max_product(lst)’ that takes a list ‘lst’ of integers and returns the maximum product of any two distinct elements from the list. The list can contain both positive and negative integers.

Input Format:
A list of integers.
Output Format:
The maximum product of any two distinct elements from the list.
Constraints:
The list will contain at least two integers.
The integers in the list may be positive, negative, or zero.
'''

# Import literal_eval library to safely evaluate string input as a Python
from ast import literal_eval

# Taking input  
lst = literal_eval(input())

def max_product(lst):
    # Write your code here
    if len(lst) < 2:
        return "List must contain at least two elements."
    lst.sort(reverse=True)
    return max(lst[0] * lst[1], lst[-1]*lst[-2])

# Print the output
print(max_product(lst))