n = input("enter the string : ")

d = ""
for i in range(len(n)):

    if n[i] not in d:
        d += n[i]
        print(f" {n[i]} : {n.count(n[i])}")