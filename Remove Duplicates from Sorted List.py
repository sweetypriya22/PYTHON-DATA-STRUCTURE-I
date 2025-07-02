#Remove Duplicates from Sorted List
'''
Write a function ‘remove_duplicates(lst)’ that removes duplicates from a sorted list. The function should modify the list in-place and return the length of the list after removing duplicates.

Input Format:
A sorted list of integers 'lst'.
Output Format:
An integer representing the new length of the list after removing duplicates.
Constraints:
The input list will be sorted.
The list will contain at least 0 elements.
'''
# Import literal_eval library to safely evaluate string input as a Python
from ast import literal_eval  

# Taking input
lst = literal_eval(input())

def remove_duplicates(lst):
    if not lst:
        return 0
   # Write your code here
    count = []
    for i in lst:
        if i not in count:
            count.append(i)
    return len(count)
# Print the output
print(remove_duplicates(lst))