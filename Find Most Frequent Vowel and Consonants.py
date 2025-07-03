'''
Write a program that takes a string 's' consisting of only lowercase English letters (from 'a' to 'z') and performs the following operations:

Identify the vowel (one of 'a', 'e', 'i', 'o', or 'u')  that appears with the highest frequency in the string.
Identify the consonant (i.e., all other lowercase letters except vowels) that appears with the highest frequency.
Compute and return the sum of the frequencies of the most frequent vowel and the most frequent consonant.

Note: If multiple vowels or consonants have the same maximum frequency, you may choose any one of them.
The frequency of a letter 'x' is the number of times it occurs in the string.
'''
s = input()
def sum_count_vov_con(s):
    vov = "aeiou"
    count = 0
    count1 = 0
    New = set()
    New1 = set()
    if s.isalpha():
        s = s.lower()
        for i in s:
            if i in vov  and i not in New :
                New.add(i)
                count+=1
            elif i not in vov and i not in New1:
                    New1.add(i)
                    count1+=1
    return count + count1
print(sum_count_vov_con(s))