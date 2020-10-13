"""
Write a program that:
- takes an input from user (number)
- if number is > 0, print "[number] is positive"
- if nuumber is < 0, "[number] is negative"
- if number is == 0, "[number} is zero"
- use if, elif, else
"""

inp = input("Enter a number")
inp = int(inp)

if (inp > 0):
    print(inp, "is positive")
elif (inp < 0):
    print(inp, "is negative")
else:
    print(inp, "is zero")