#Check for Balanced Parentheses
'''
Write a function ‘is_balanced(s)’ that checks if the parentheses in the given string are balanced. The function should also check for balanced brackets [] and curly braces {} in addition to the regular parentheses ().

A string is considered balanced if:
Every opening bracket has a corresponding closing bracket.
The brackets are closed in the correct order.

Input Format:
A single string ‘s’ consisting of characters such as (, ), {, }, [, ], and other non-bracket characters.
Output Format:

True if the string has balanced brackets and False otherwise.
'''
# Taking input
s = input()

def is_balanced(s):
    stack = []  # This is your bracket tracker!
    pairs = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()

    return len(stack) == 0

# Print the output
print(is_balanced(s))