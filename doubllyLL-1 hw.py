class node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

class doubllyLL:
     def __init__(self):
         self.head = None

     
     def display(self):
        if self.head is None:
            print("list is empty")
            return
        temp = self.head
        while temp:
            print(temp.data, "-->", end=" ")
            temp = temp.next


l = doubllyLL()
n = node(10)
l.head = n
n1 = node(20)
n.next =n1 
n2 = node(30)
n2.prev = n1
n1.next =n2
l.display()
