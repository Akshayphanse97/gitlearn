def is_palimdrom(a):
    # d=""
    # for i in range(len(a)-1,-1,-1):
    #     d+=a[i]
    d = a[::-1]
    
    if a==d:
        return True
    return False
    



n =  input("enter the palimdrom string")

print(is_palimdrom(n))
