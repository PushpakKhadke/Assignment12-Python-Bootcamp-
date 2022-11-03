# 1. Write a python script to reverse a number.

Number = int(input("Enter The Number : "))
i = 0
while Number!= 0:
    a = Number % 10
    i = i*10+a
    Number//=10
print("Reversed Number is :",i)


"""
2nd Way!

Number=int(input("Enter The Number: "))
while (Number):
    print(Number % 10, end='')
    Number //= 10
"""

