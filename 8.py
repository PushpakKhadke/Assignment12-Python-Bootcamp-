"""
8. Write a python script to print first N terms of a Fibonacci series
"""

Number=int(input("Enter Number: "))
A=-1
B=1
C=A+B
for x in range(1,Number+1):
    print(C)
    A=B
    B=C
    C=A+B
