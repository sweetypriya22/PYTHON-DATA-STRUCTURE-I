#Unique Triplets Sum to Zero
'''
Write a program that defines a function 'count_above_average(numbers)' which returns the count of elements in the list that are strictly greater than the average of all elements.

Input Format:
A single line containing a list of integers.
Output Format:
A single integer that represents the count of elements strictly greater than the average of the list.
Constraints:

The list contains at least 1 and at most 100 integers.
Each integer lies between -10⁵ and 10⁵.
'''
# Import literal_eval library to safely evaluate string input as a Python
from ast import literal_eval

# Taking input
numbers = literal_eval(input())

def count_above_average(numbers):
    # Write your code here
    avg = sum(numbers) / len(numbers)
    count = sum(1 for i in numbers if i>avg)
    return count
# Print the output
print(count_above_average(numbers))