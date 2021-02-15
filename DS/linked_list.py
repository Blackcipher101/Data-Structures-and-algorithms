
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
    def push(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
            self.head = new_node
    def insertAfter(self, prev_node, new_data):
        if prev_node is None:
            print ("the given previous node cannot be NULL")
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node
        if new_node.next:
            new_node.next.prev = new_node
    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while True:
            if last.next == None:
                last.next=new_node
                new_node.prev=last
                return
            last = last.next
    def printList(self, node):
        print ("\nTraversal in forward direction")
        while node:
            print ((node.data))
            node = node.next
    def delete_node(self, node,ele):
        while node:
            if ele==node.data:
                node.prev.next = node.next
                node.next.prev = node.prev
            node = node.next


llist = DoublyLinkedList()

llist.append("Goa")
llist.printList(llist.head)

llist.push("Paris")

llist.push("Ghana")


llist.append("Ibiza")

print ("Created DLL is:Before Adding ")
llist.printList(llist.head)
llist.insertAfter(llist.head.next, "Kerela")
print ("Created DLL is: After adding")
llist.printList(llist.head)

llist.delete_node(llist.head,"Kerela")
print ("Created DLL is: after deleting")
llist.printList(llist.head)

llist.head.data ="London"
llist.printList(llist.head)









