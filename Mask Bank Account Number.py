#Mask Bank Account Number
'''
Write a function 'mask_account(account)' that takes a bank account number as a string.
The function should return a masked version of the account number where:

The first four digits remain unchanged.
The last four digits remain unchanged.
All characters between the first four and last four digits are replaced with the asterisk character (*).
Input Format:
A single string account representing a bank account number.
'''
# Taking input
account = input()

def mask_account(account):
    # Write your code here
    if len(account)<8:
        return "Invalid account number"
    
    masked_account = account[:4] + '*' * (len(account) - 8) + account[-4:]
    return masked_account
# Print the output
print(mask_account(account))