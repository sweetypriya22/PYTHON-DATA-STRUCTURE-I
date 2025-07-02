#Anagram Check
'''
Write a function ‘are_anagrams(str1, str2)’ that takes two strings ‘str1’ and ‘str2’ as input and returns True if they are anagrams of each other, and False otherwise. The function should be case-insensitive and should ignore spaces between words.
An anagram is when two strings contain the same characters, but possibly in a different order.

Input Format:
Two strings, ‘str1’ and ‘str2’, which may contain spaces and are case-insensitive.

Output Format:
True if the two strings are anagrams, and False otherwise.
'''
# Taking input
str1 = input()
str2 = input()

def are_anagrams(str1, str2):
    # Write your code here
    lst1 = str1.replace(" ", "").lower()
    lst2 = str2.replace(" ", "").lower()

    if sorted(lst1)== sorted(lst2):
        return True
    else: 
        return False
# Print the result
print(are_anagrams(str1, str2))