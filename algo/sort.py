def bubblesort(arr):
    n=len(arr)
    for i in range(n):
        for j in range (0,n-i-1):
            if arr[j]>arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp

Array=[78,34,46,420,8,7,51,32,1,21,5,29,19,66]
bubblesort(Array)
print("Sorted array by Bubblesort:\n")
print(Array,'\n')
#Selection sort
def selectionSort(arr, size):
   
   for step in range(size):
        max_index = step
        for i in range(step + 1, size):
            if arr[i] < arr[max_index]:
                max_index = i
         
       
        (arr[step], arr[max_index]) = (arr[max_index], arr[step])


array = [78,34,46,420,8,7,51,32,1,21,5,29,19,66]
size = len(array) 
selectionSort(array, size)
print('Sorted array by Selection sort:\n')
print(array,'\n')

#insertion sort
def insertionSort(arr):
    for step in range(1, len(arr)):
        key = arr[step]
        j = step - 1
           
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key
array = [78,34,46,420,8,7,51,32,1,21,5,29,19,66]
insertionSort(array)
print('Sorted Array by insertion sort:\n')
print(array,'\n')
