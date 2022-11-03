"""
7. Write a python script to check whether a given pair of numbers are co-Prime
numbers or not.
"""

First_Number = int(input("Enter The First Number : "))
Second_Number = int(input("Enter The Second Number : "))
ab = min(First_Number,Second_Number)
for i in range (1,ab+1):
    if First_Number%i==0 and Second_Number%i==0:
        xyz=i

if xyz==1:
    print("This is a co-prime number")

else:
    print("This is not a co-prime number")






