first=int(input("Enter the first range:"))
second=int(input("Enter the last range:"))
list=[]
for i in range(first,second):
    if i%2==0:
        for j in range(1,i):
            if j*j==i:
                list.append(i)
print(list)
if len(list)==0:
    print(list)