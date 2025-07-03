#All Indices of Target Element
'''
Write a function that returns a list of all indices where the target element occurs in the list.
The program should return the indices in ascending order. If the target does not appear in the list, return an empty list.

Input Format:

An integer n, representing the number of elements in the list.
A list of n integers.
An integer target, the element to find.
'''
# Import the literal_eval library to safely evaluate string input as a Python 
from ast import literal_eval

# Taking input
n = int(input())
lst = literal_eval(input())
target = int(input())


def find_all_indices(lst, target):
    # Write your code here
    New = []
    for i in range(len(lst)):
        if lst[i] == target:
            New.append(i)
        
    return New
# Print the output  
print(find_all_indices(lst, target))