class Node:
    def __init__(self, val, node = None):
        self.next = node
        self.val = val
        
class LinkedList:
    node = None
    
    def addNode(self, val):
        new_node = Node(val)
        
        if self.node == None:
            self.node = new_node
        else:
            tmp = self.node
            while tmp.next != None:
                tmp = tmp.next
            tmp.next = new_node
    
    def printNode(self):
        tmp = self.node
        while tmp != None:
            print(tmp.val)
            tmp = tmp.next
            

a = [1, 2, 3, 4, 5]

ls = LinkedList()

for n in a:
    ls.addNode(n)
    
ls.printNode()
