import singly_linkedlist
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Linkedlist:
    def __init__(self):
        self.head = None

    def Reverse_linkedlist(self):
        currrent = self.head
        prev = None
        while currrent !=None:
            temp = currrent.next
            prev = currrent
            currrent = temp
        return prev
    

