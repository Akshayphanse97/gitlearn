l=['abc','efg','xyz']

list_2 = [i[::-1] for i in l]
print(list_2)


l2=['akshay','ayd',1,2,3,4,5.6,9.6,]
# print(l2)
list_3 = [ str(i) for i in l2 if type(i) == int or type(i) == float ]
print(list_3)

l3=[i*2 if (i%2==0) else -i for i in range(1,11) ]
print(l3)
