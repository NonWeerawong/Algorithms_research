class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    # function to create a linkedlist by inserting value at the end
    def insertNode(self, val):
        newNode = Node(val)
        if self.head == None:
            # print("DEBUG: head is None")
            self.head = newNode
        else:
            # print("DEBUG: head isn't None")
            self.tail.next = newNode
        self.tail = newNode
    def deleteNode(self, idx):
        tmp = self.head
        if (tmp != None and idx == 0):
            self.head = tmp.next
        else:
            prev = self.head
            p = 0
            while (tmp != None and p < idx):
                prev = tmp
                tmp = tmp.next
                p += 1
            if (tmp != None):
                prev.next = tmp.next

    # print LinkedList line by line
    def printList(self):
        # print(type(self.head))
        tmp = self.head
        while (tmp != None):
            print(tmp.val)
            tmp = tmp.next

l1 = LinkedList()

for val in [1, 2 ,3, 4 ,5]:
    l1.insertNode(val)
    
l1.printList()
l1.deleteNode(2)
print("#############")
l1.printList()

