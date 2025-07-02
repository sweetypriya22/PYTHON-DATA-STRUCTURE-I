#Check Isomorphic Strings
'''
Given two strings s and t, write a program to determine if they are isomorphic.
Two strings 's' and 't' are isomorphic if the characters in 's' can be replaced to get 't'.
All occurrences of a character must be replaced with another character
while preserving the order of characters. 
No two characters may map to the same character, but a character may map to itself.
'''
s = input().strip()
t = input().strip()

def are_isomorphic(s, t):
    if len(s) != len(t):
        return False

    map_s_t = {}
    map_t_s = {}

    for ch_s, ch_t in zip(s, t):
        if map_s_t.get(ch_s, ch_t) != ch_t or map_t_s.get(ch_t, ch_s) != ch_s:
            return False
        map_s_t[ch_s] = ch_t
        map_t_s[ch_t] = ch_s

    return True

print(are_isomorphic(s, t))