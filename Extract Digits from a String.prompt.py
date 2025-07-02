#Extract Digits from a String
'''
Write a program that extracts all the digits from a given string and returns them as a list of integers.

Input Format:
A string 's' will consist of ASCII characters.
Output Format:
A list of integers.
'''
# Taking input
s = input()

def extract_digits(s):
    # Write your code here
    return [int(char) for char in s if char.isnumeric()]

# Print the output
print(extract_digits(s))