 
def printRepeating(arr, size):
 
    print("The repeating elements are: ")
 
    for i in range(0, size):
        
        print('Loop'+ str(i) + '  '+ str(arr[abs(arr[i])]))
        if arr[abs(arr[i])] >= 0:
            arr[abs(arr[i])] = -arr[abs(arr[i])]
            print(arr[abs(arr[i])])
        else:
            print(abs(arr[i]), end=" ")
 
 
# Driver code
arr = [1, 2, 3, 1, 3, 6, 6]
print(arr[0])
arr_size = len(arr)
 
printRepeating(arr, arr_size)