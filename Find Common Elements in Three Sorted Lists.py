'''
Write a program that accepts three sorted lists of integers as input and returns a list containing the elements that are common to all three lists.
The program should be implemented efficiently, taking advantage of the fact that the input lists are already sorted. Avoid using unnecessary nested loops, and do not use sets or any external libraries that are not part of the standard Python curriculum up to this point.
If there are no common elements among the three lists, the program should output "None" (without quotes
'''

# Import the literal_eval library to evaluate string input as a Python safely 
from ast import literal_eval

# Taking input
list1 = literal_eval(input())  
list2 = literal_eval(input())  
list3 = literal_eval(input())  

# Efficient linear traversal using three pointers
def find_common_elements(l1, l2, l3):
    # Write your code here
    result = []
    for num in list1:
        if num in list2 and num in list3 and num not in result:
            result.append(num)
    return result
    
common_elements = find_common_elements(list1,list2,list3)
    



# Print the output
print(" ".join(map(str, common_elements)) if common_elements else "None")

