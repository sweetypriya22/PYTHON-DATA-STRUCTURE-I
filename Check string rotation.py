'''
You are given two strings, 's1' and 's2'. Write a program to check if 's2' is a rotation of 's1'.
Two strings are said to be rotations of each other if they contain the same characters in the same order but starting from a different position
and wrapping around. For example, "erbottlewat" is a rotation of "waterbottle" because the characters from the start have been shifted to the end.
'''
def is_rotation(s1, s2):
    if len(s1) != len(s2):
        return False
    return s2 in (s1 + s1)

result = is_rotation(s1, s2)

# Print the Output
print("Yes" if result else "No")