class node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DobullyLL:
    def __init__(self):
        self.head = None

    def search(self, data):
        temp = self.head
        while temp:
            if temp.data == data:
                print("element found")
                return
            temp = temp.next
        print("no value found")

    def insert_at_position(self, data, pos):
        newnode = node(data)

        if pos == 1:
            if self.head:
                newnode.next = self.head
                self.head.prev = newnode
            self.head = newnode
            return

        temp = self.head
        count = 1

        while temp and count < pos - 1:
            temp = temp.next
            count += 1

        if temp is None:
            print("position out of range")
            return

        newnode.next = temp.next
        newnode.prev = temp

        if temp.next:
            temp.next.prev = newnode

        temp.next = newnode

    def display(self):
        if self.head is None:
            print("list is empty")
            return
        temp = self.head
        while temp:
            print(temp.data, "-->", end=" ")
            temp = temp.next


# Driver code
l = DobullyLL()

n = node(10)
l.head = n

n1 = node(20)
n.next = n1
n1.prev = n

n2 = node(30)
n1.next = n2
n2.prev = n1

l.display()
print("\n")

l.insert_at_position(25, 3)
l.display()
print("\n")

l.search(100)
l.search(20)
