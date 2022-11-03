# 2. Write a python script to check whether a given number is Prime or not

Number=int(input("Enter The Number: "))
for i in range(2,Number):
    if(Number%i==0):
        print("Not Prime Number")
        break
else:
    print("Prime Number")
