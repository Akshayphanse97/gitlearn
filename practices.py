# n=int(input("enter the number"))

# factorial=1

# if n==0:
#     print(factorial)
# elif n==1:
#     print(factorial)
# else:
#     for i in range(1,n+1):
#         factorial *=i
#     print(factorial)


# num1=0
# num2=1
# print(num1,num2,end=' ')
# for i in range(2,n+1):
#     sum=num1+num2
#     print(sum,end=' ')
#     num1=num2
#     num2=sum
# print()    

# l=[20,50,70,41,2]

# min=l[0]
# max=l[0]
# for i in range(1,len(l)):
#     if l[i]<min:
#         min=l[i]
#     elif l[i]>max:
#         max=l[i]
# print("min",min)
# print("max",max)

# l1=[10,20,30,40,50]
# d=l1[0]
# l1[0]=l1[-1]
# l1[-1]=d
# print(l1)

# s='nananrg'
# d=(set(s))
# e=("".join(d))
# str(e)
# print(type(e))

n ="sky is blue"
print(" ".join(n.split()[::-1]))

list1=[1,2,3,4,4,3,2,7]
new_list=[]
for i in list1:
    if i not in new_list and list1.count(i)==1:
        new_list.append(i)
        print(new_list)            

print([i for i in list1 if list1.count(i)==1])


y='a,b,a,b,a,b,c,c,d,f'
f=y.split(",")
print({key:f.count(key) for key in f })


l=list('hello')
p=l[0],l[-1],l[1:3]
a='a={0},b={1},c={2}'.format(*p)
print(a)