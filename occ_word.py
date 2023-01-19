s=input("Enter a text:").split()
a=list(set(s))
for i in a:
    print(i,"-",s.count(i))