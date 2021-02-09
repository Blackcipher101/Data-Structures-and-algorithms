class Deque:

def __init__(self):

self.items = []

def isEmpty(self):

return self.items == []

def addFront(self, item):

self.items.append(item)

def addRear(self, item):

self.items.insert(0,item)

def removeFront(self):

return self.items.pop()

def removeRear(self):

return self.items.pop(0)

def size(self):

return len(self.items)

dq = Deque()

arr = [12,35,36,1,38,98]

print("adding to rear") # array=[12]

dq.addRear(arr[0])

print(arr[0])

print("adding to front") # arary=[12,35]

dq.addFront(arr[1])

print(arr[1])

print("adding to rear")

dq.addFront(arr[2]) #array=[36,12,35]

print(arr[2])

print("adding to rear")

print(arr[4])

dq.addRear(arr[4]) #array=[36,12,38]

print("remove from front")

print(dq.removeFront() ) #array=[36,12]

print("remove from back")

print(dq.removeRear()) #array=[36,12]