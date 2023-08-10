class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        newNode = Node(data)
        if (self.head):
            current = self.head
            while (current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

    def printLL(self):
        current = self.head
        while (current):
            print(current.data)
            current = current.next


if __name__ == '__main__':
    L = LinkedList()
    L.insert(3)
    L.insert(4)
    L.insert(5)
    L.printLL()