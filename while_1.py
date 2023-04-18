# n =  int(input("enter the number "))

# total = 0
# i=1
# while i<=n:
#     total += i
#     i +=1
# print(f" total n number of {total}")


d = input(" enter number more than one digit")

total = 0
i=0
while len(d)>i:
    total= total + int(d[i])
    i+=1
print(f"sum of digit {total}")


