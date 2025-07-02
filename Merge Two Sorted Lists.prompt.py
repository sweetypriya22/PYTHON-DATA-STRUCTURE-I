#Merge Two Sorted Lists
'''
Write a program that merges two sorted lists of integers into a single sorted list. The merged list should contain all elements from both lists, sorted in ascending order. 
Input Format:
Two sorted lists of integers, each sorted in ascending order.
The lists can contain any number of integers and will not contain nested lists.
Output Format:
A single list containing all the elements from both input lists, sorted in ascending order. 

'''
from ast import literal_eval
# Import the literal_eval function from the ast library to safely evaluate string input as a Python list
from ast import literal_eval

# Taking input  
list1 = literal_eval(input())
list2 = literal_eval(input())

def merge_sorted_lists(list1, list2):
    # Write your code here
    New = list1 + list2
    New.sort()
    return New

# Print the output
print(merge_sorted_lists(list1, list2))