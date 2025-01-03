def find_index(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index
    return None

testcase_n = int(input())

for i in range(testcase_n):
    arr_size = int(input())
    score = 0
    arr = list(map(int, input().split()))
    while len(arr)!=0:
        target = arr.pop(0)
        index = find_index(arr,target)
        
        if index!=None:
            score += 1
            arr.pop(index)
    print(score)
    