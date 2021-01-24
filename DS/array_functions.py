example=[1,3,4,2,6,7]
list2=[2 , 2]
example.append(9) # append method adds the element at the end of the list
print("The list is appended with 9 at the end:")
print(example)
example.pop() # pop method removes the last element from the list 
print("The last element is removed from the list:")
print(example)
example.insert(2 ,2) # insert method inserts the element at the specified postion (postion, element) 
print("The element is added to the list at the second index")
print(example) 
example.sort() # the method sorts the list in an ascending order
print("The list is sorted")
print(example)
example.extend(list2) # This addes on the specied list to the new list
print("The list is extended with list2")
print(example)
count=example.count(2) # this method returns the count of the element 
print("The count of 2 is printed")
print(count)
