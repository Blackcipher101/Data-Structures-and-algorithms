 
class Node: 
 
	def __init__(self, data): 
		self.data = data  
		self.next = None 



class LinkedList:
    def __init__(self): 
        self.head = None
    def printList(self):
        temp = self.head 
        while (temp): 
            print (temp.data) 
            temp = temp.next


 
llist = LinkedList() 

llist.head = Node("Goa") 
second = Node("Paris") 
third = Node("Spain")
fourth = Node("Iceland")

fifth = Node("Greece") 
sixth = Node("Ibiza")  
seventh = Node("Ghana") 
eighth = Node("Egypt") 

llist.head.next = second
second.next = third
third.next = fourth
fourth.next = fifth
fifth.next = sixth
sixth.next = seventh
seventh.next = eighth
llist.printList()
newNode = input("new place")

ninth=Node(newNode)

eighth.next = ninth

print("\n\n\n #################################### \n\n\n")

llist.printList()

fifth.next=seventh  #removing sixth Ibiza

print("\n\n\n #################################### \n\n\n")

llist.printList()
eighth.next = third.next
second.next = eighth
seventh.next = third
third.next = None
print("\n\n\n #################################### \n\n\n")

llist.printList()




