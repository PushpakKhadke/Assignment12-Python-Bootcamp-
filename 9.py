"""
9. Write a python script to calculate LCM of two numbers
"""

First_Number=int(input("Enter First Number : "))
Second_Number=int(input("Enter Second Number : "))
for a in range (First_Number,(First_Number*Second_Number)+1,1):
    if(a%First_Number==0 and a%Second_Number==0):
          break
print(f"LCM of {First_Number} and {Second_Number} is :",a)
