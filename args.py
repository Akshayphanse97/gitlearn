def square(num,*args):
    if len(args) == 0:
        return "hey you did not pass  args"
    else:
         l1 = [i**num for i in args]
         return l1
l=[1,2,3]
print(square(3,*l))    


def first_cap(*args):
    return [i.title() for i in args]



l2=['akshay','amar','omkar']
print(first_cap(*l2))

help(min)
print(sorted.__doc__)

def mobile(l):
    total=0
    for i in l:
        total+=int(i)
    # total.split()
    return total
l=list(input("enter the mobile number"))
print(mobile(l))

