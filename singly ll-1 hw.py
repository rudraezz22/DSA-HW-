class node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLL:
    def __init__(self):
        self.head = None

    def search(self, data):
        t = 0
        temp = self.head

        while temp:
            if temp.data == data:
                t = 1
                break
            temp = temp.next

        if t == 1:
            print("element found")
        else:
            print("no value found")

    def display(self):
        if self.head is None:
            print("list is empty")
            return

        temp = self.head
        while temp:
            print(temp.data, "-->", end=" ")
            temp = temp.next


# Driver code
l = SinglyLL()

n = node(10)
l.head = n

n1 = node(20)
n.next = n1

n2 = node(30)
n1.next = n2

l.display()
print("\n")

l.search(100)
l.search(20)
