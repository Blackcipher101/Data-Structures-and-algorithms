class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

print("The Queue")
q = Queue()
arr = [12,35,36,1,38,98,45,46,93,56]
for i in range (10):
    q.enqueue(arr[i])
    

for i in range (10):
    print(q.dequeue(), end=" ")

s = Stack()
print("\nThe Stack")
for i in range (10):
    s.push(arr[i])
    

for i in range (10):
    print(s.pop(), end=" ")