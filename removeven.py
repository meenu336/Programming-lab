n=int(input("Enter the list of elements:"))
print("Enter the elements:")
list=[]
for i in range(0,n):
    ele=int(input())
    if (ele%2!=0):
        list.append(ele)
print(list)