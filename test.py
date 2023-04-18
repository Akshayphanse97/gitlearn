n=input("enter the string ")
rev=""
for i in n:
    rev=i+rev
if rev == n:
    print("palimdrom string")
else:
    print("this not palimdrom") 

