def distinctarr(arr):
    if not arr:
        return 0

    j = 0
    for i in range(1, len(arr)):
        if arr[i] != arr[j]:
            j += 1
            arr[j] = arr[i]

   
    for k in range(j + 1, len(arr)):
        arr[k] = None

    return j + 1


arr1 = [1, 1, 2]
print(distinctarr(arr1))  

arr2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(distinctarr(arr2)) 

print(arr1)  
print(arr2) 
