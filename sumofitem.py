n=int(input("Enter the limit:"))
list=[]
sum=0
print("Enter the elements in the list:")
for i in range(n):
    ele=int(input())
    list.append(ele)
    sum=sum+list[i]
print(list)
print("sum of items:",sum)