x=int(input("Enter the starting year:"))
y=int(input("Enter the ending year:"))
print("The following leap years are:")
for i in range(x,y):
    if((i%400==0) or ((i%100!=0) and (i%4==0))):
        print(i)
