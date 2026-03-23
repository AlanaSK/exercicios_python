# bubble sort

arr = [45, 3, 14, 2, 25, 48, 36, 4]
arr_length = len(arr)

def bubble_sort(arr: list[int]):
    for i in range(arr_length): 
        swapped = False
        for j in range(0, arr_length - i - 1): 
            if arr[j] > arr[j+1]:
                swapped = True
                arr[j], arr[j+1] = arr[j+1], arr[j]
            if not swapped:
                break
print(arr)