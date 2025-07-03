'''
Write a program that defines a function 'longest_word(sentence)' 
which returns the longest word in the sentence. 
If multiple words have the same maximum length, return the first one among them.

Input Format:
A single line containing a sentence with words separated by spaces.
Output Format:
A single word that is the longest in the sentence.
'''
sentence = input()
def longest_word(sentence):
    words = sentence.split()
    longest = max(words, key=len)
    return longest
print(longest_word(sentence))