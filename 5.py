# 5. Write a python script to find next prime number of a given number

Number=int(input("Enter The Number : "))
for i in range(Number+1,Number+20,1):
    for a in range(2,(i//2+1)):
        if i%a==0:
            break
    else:
        print(i)
        break

