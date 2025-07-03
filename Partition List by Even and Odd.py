'''
Write a program to rearrange the list such that all even numbers appear before all odd numbers. The relative order of even and odd numbers should be preserved as in the original list.



Input Format:

An integer 'n', the number of elements in the list.
A list of 'n' integers

'''
# Import the literal_eval library to safely evaluate string input as a Python 
from ast import literal_eval

# Taking input
n = int(input())
arr = literal_eval(input())

def partition_even_odd(arr):
    # Write your code here
    Even = []
    Odd = []
    for i in arr:
        if i%2==0:
            Even.append(i)
        else:
            Odd.append(i)
    return Even + Odd
# Print the output
print(partition_even_odd(arr))
