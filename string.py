#Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string.

string=input("Enter String: ")
result=""

if len(string)<2:
    print(result)
    
else:
    result+=string[:2]
    result+=string[len(string)-2:]
    print(result)
