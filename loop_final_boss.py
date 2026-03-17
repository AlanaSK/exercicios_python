arr = [45, 3, 14, 2, 25, 48, 36, 4]
arr_lenght = len(arr)

for i in range(arr_lenght): 
    for j in range(0, arr_lenght - i - 1): 
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
print(arr)
        