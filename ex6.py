name,age = input("enter the name and age :").split(",")

if name[0] =='a' or name[0]=='A' and int(age)>10:
    
    print("you watch movies")

else:
    print("sorry you cannnot watch movies")