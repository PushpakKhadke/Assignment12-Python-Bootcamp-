# 3. Write a python script to print all Prime numbers under 100

for i in range(2,101,1):
    Flag=0
    for a in range(2,(i//2+1)):
        if i%a==0:
            break
    else:
        print(i,end=" ")

"""
# 2nd Way!
for i in range(2,101):
    if a (i%p for p in p):
        print(i,end=" ")
        p.append(i) 
"""