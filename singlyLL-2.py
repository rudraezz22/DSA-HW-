class node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLL:
    def __init__(self):
        self.head = None

    def reverse(self):
        prev = None
        curr = self.head

        while curr:
            nextnode = curr.next
            curr.next = prev
            prev = curr
            curr = nextnode

        self.head = prev

    def display(self):
        if self.head is None:
            print("list is empty")
            return

        temp = self.head
        while temp:
            print(temp.data, "-->", end=" ")
            temp = temp.next
        print("NULL")


# Driver code
l = SinglyLL()

n = node(10)
l.head = n

n1 = node(20)
n.next = n1

n2 = node(30)
n1.next = n2

print("Before reversing:")
l.display()

l.reverse()

print("After reversing:")
l.display()
