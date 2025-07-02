'''
Write a program that takes a string as input and counts the number of vowels and consonants in it. 

Vowels include
 'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'.
Consonants are all other alphabetic letters (i.e., all letters except vowels).
All non-alphabetic characters (e.g., spaces, digits, punctuation) in the input string should be disregarded.

'''
# Taking input
s = input()

def count_vowels_and_consonants(s):
    # Write your code here
    vov = 'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'
    vowels = 0
    consonants = 0
    for i in s:
        if i.isalpha():
            if i in vov:
                vowels+=1
            else:
                consonants+= 1
    return vowels, consonants
# Print the Output
vowels, consonants = count_vowels_and_consonants(s)
print(vowels)
print(consonants)
