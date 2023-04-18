def rev_list(l):
    a=[]
    for i in range(len(l)):
        a.append(l.pop())
    return a

list1=list(range(1,11))
# print(list1)
print(rev_list(list1))
