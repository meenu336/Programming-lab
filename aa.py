n=int(input("Enter the number of elements:"))
print("Enter the names:")
list=[]
count=0
for i in range(0,n):
    ele=input()
    list.append(ele)
    print(list)
    for i in list:
        for j in i:
            if j=='a':
                count=count+1
    print(count)