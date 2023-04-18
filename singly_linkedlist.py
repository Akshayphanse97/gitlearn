class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def insert_biginning(self,data):
        newnode = Node(data)
        newnode.next = self.head
        self.head = newnode 

    def insert_last(self,data):
        newnode = Node(data)
        if self.head == None:
            self.head=newnode
            return
        temp = self.head
        while temp.next!=None:
            temp=temp.next
        temp.next = newnode
    
    def middle_insert(self,node,data):
        if self.head == None:
            print("this linked list is empty")
            return
        newnode = Node(data)
        newnode.next= node.next
        node.next = newnode 

    def deletebegining(self):
        if self.head == None:
            print("linked list is empty")
            return
        
        self.head = self.head.next

    def deletelast(self):
        if self.head == None:
            print("linked list is empty")
            return
        temp = self.head
        while temp.next:
            temp=temp.next
            if temp.next.next == None:
                temp.next = None
    def Reverse_linkedlist(self):
        currrent = self.head
        prev = None
        while currrent !=None:
            temp = currrent.next
            prev = currrent
            currrent = temp
        return prev

    def Display(self):
        temp= self.head
        while temp:
            print(temp.data,end=' ')
            temp=temp.next

n = Linkedlist()
n.insert_biginning(1)
n.insert_biginning(2)
n.insert_last(5)
n.middle_insert(n.head.next,'hello')
# n.deletebegining()
# n.deletelast()
# n.Display()
n.Reverse_linkedlist()
n.Display()

l= int(25.6)
print(type(l),l)
