

def binary_sort():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    low = 0
    high = len(numbers) - 1
    while low <= high:
        mid = (low + high) // 2
        if numbers[mid] == 5:
            break
        elif numbers[mid] < 5:
            low = mid + 1
        else:
            high = mid - 1
    numbers.sort()

binary_sort()