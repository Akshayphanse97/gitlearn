# n = input("enter the string :")

# i=0
# temp_var =""
# while i < len(n):
#     if n[i] not in temp_var:
#         temp_var+=n[i]
#         print(f" {n[i]} : {n.count(n[i])}")
#     i+=1


n = input("enter the number")

total = 0

for i in range(len(n)):

    total +=int(n[i])
print(f" sum of numer of digit {total}")