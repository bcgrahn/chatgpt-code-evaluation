

def binary_sort():
    arr = [7, 3, 5, 1, 6, 4, 2]
    l = len(arr)
    for i in range(l):
        for j in range(0, l-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

binary_sort()