#longest word
sen=input("Enter the words:")
longest=max(sen.split(),key=len)
print("longest word is:",longest)
print("its length is:",len(longest))