# 6. Write a python script to print first N prime numbers

Number= int(input("Enter the Number : "))
i = 2
while Number!=0:
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i,end=" ")
        Number -=1
    i +=1