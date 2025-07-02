#Longest Non-Repeating Substring
'''
You are given two lists of integers; 'list1' and 'list2'. Merge these lists into one sorted list and return the median value.

If the total number of elements is odd, return the middle element.
If even, return the average of the two middle elements.
This task requires handling both odd and even-length combined lists.

Input Format:
Two lines:
A list of integers (list1)
Another list of integers (list2)
Output Format:
A single float or integer representing the median
'''

# Import literal_eval library to safely evaluate string input as a Python
from ast import literal_eval

# Taking input
list1 = literal_eval(input())
list2 = literal_eval(input())

def find_median_lists(list1, list2):
    # Write your code here
    if 1<=len(list1) + len(list2)<=1000:
        sort_list = list1 + list2
        sort_list.sort()
        if len(sort_list) % 2==1:
            return sort_list[len(sort_list)//2]
        else:
            a1 = sort_list[len(sort_list)//2-1]
            a2 = sort_list[len(sort_list)//2]
            avg = (a1+a2)/2
            return avg
 
# Print the output
print(find_median_lists(list1, list2))