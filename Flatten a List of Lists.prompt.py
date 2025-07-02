#Flatten a List of Lists
'''
Write a program that flattens a nested list into a single list using List Comprehension. The program should take the nested list as input and return the flattened version of the list.
Input Format:
A nested list.

Output Format:
A flattened list that contains all the elements from the sublists of lists in the same order.
'''

from ast import literal_eval

# Taking input
lists = literal_eval(input())

def flatten_lists(lists):
    # Write your code here
    return [j for i in lists for j in i ]

# Print the output
print(flatten_lists(lists))