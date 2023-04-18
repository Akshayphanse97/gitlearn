def filter_odd_even(l):
    odd_even=[[],[]]

    for i in l:
        if i%2==0:
            odd_even[0].append(i)
        else:
            odd_even[1].append(i)
    return odd_even

list1= list(range(1,11))
print(filter_odd_even(list1))
