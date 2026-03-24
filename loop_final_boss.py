# bubble sort

arr = [45, 3, 14, 2, 25, 48, 36, 4]

def bubble_sort(arr: list[int]):
    arr_length = len(arr)
    for i in range(arr_length): 
        for j in range(0, arr_length - i - 1): 
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
bubble_sort(arr)
print(arr)