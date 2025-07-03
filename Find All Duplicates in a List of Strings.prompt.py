'''
Write a function 'find_duplicate_strings(input_list)' that accepts a list of strings. The function must identify and return a new list containing only those strings that occur at least twice within the 'input_list'. The returned list must consist of unique strings, ordered by their first appearance as a duplicate in the original 'input_list'.



Input Format:

A list of strings, where each string contains only lowercase or uppercase alphabetical characters.
The list can contain duplicate entries.
'''
# Import the literal_eval library to evaluate string input as a Python safely 
from ast import literal_eval

# Taking input
lst = literal_eval(input())

def find_duplicates(lst):
    # Write your code here
    New = []
    repeat = []
    for i in lst:
        if i in New:
            if i not in repeat:
                repeat.append(i)
        else:
            New.append(i)
        
    return repeat

# Print the output 
print(find_duplicates(lst))