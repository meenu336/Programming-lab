list1=[13,43,-8,25,-76]
list2=[45,-76,56,4,25]
x=len(list1)
y=len(list2)
s1=sum(list1)
s2=sum(list2)
if(x==y):
    print("The two list have same length")
else:
    print("Different length")
if(s1==s2):
        print("sum of two lists are same")
else:
        print("sum is different")
        print("common elements")
        for i in list1:
            for j in list2:
                if(i==j):
                    print(i)
