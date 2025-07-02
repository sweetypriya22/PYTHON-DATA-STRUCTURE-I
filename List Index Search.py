'''
Write a program that takes a list of elements and finds the index of a given element in the list. 
If the element does not exist in the list, the program should return -1.
Input Format:
A list of integers.
An integer to search for in the list.

Output Format:
The index of the element in the list, or -1 if the element is not found.
Constraints:
The list will contain integers.
The search element is an integer.
'''
# Import literal_eval library to safely evaluate string input as a Python
from ast import literal_eval

# Taking input
lst = literal_eval(input())   
search_element = int(input())  

def find_index(lst, search_element):
        # Write your code here
        if search_element in lst:
                return lst.index(search_element)
        else:
                return -1

# Print the output
print(find_index(lst, search_element))
