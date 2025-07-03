'''
Write a function that takes a list of integers and returns a new list containing all elements that appear exactly twice in the list.



The result should be returned in ascending order. If no element appears exactly twice, return an empty list.



Input Format:

An integer n, the number of elements in the list.
A list of n integers.
'''
from ast import literal_eval

# Input lena
n = int(input())
lst = literal_eval(input())

def find_exactly_twice(lst):
    freq = {}
    
    # Step 1: Frequency count
    for num in lst:
        freq[num] = freq.get(num, 0) + 1

    # Step 2: Filter only those with count 2
    result = [key for key, value in freq.items() if value == 2]

    # Step 3: Sort the result
    return sorted(result)

# Output print karna
print(find_exactly_twice(lst))