x = ["apple", "banana", "cherry"]
y = x
x[0] = "mango"
print(y)

list1=[12,47,87,41]
list2=["1","2","3","4"]

data ={key:value for key,value in zip(list1,list2) if 12<int(key)<50}

print(sum(data.keys()))