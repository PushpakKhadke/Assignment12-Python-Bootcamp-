# 10. Write a python script to calculate HCF of two numbers

First_Name=int(input("Enter First Number:  "))
Second_Number=int(input("Enter Second Number : "))
for a in range(1,First_Name*Second_Number,1):
    if(First_Name%a==0 and Second_Number%a==0):
        HCF=a
print(f"HCF of {First_Name} and {Second_Number} is :",HCF)