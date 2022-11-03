# 4. Write a python script to print all Prime numbers between two given numbers (both values inclusive)

Starting_Number = int(input("Enter The Starting Number: "))
Ending_Number = int(input("Enter The Ending Number: "))

print("Prime numbers between ",Starting_Number," to ",Ending_Number," is : ")
for i in range(2,Ending_Number+1):
    n=1
    for j in range(2,i//2+1):
        if(i%j==0):
            n=0
    if n==1:
        print(i,end=" ")
