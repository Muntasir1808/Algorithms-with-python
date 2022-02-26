def ternary_search(array, element):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid1 = (low + high) // 2
        mid2 = (low + high) // 3
        if array[mid1] == element:
            return mid1
        elif array[mid2] == element:
            return mid2
        elif key < array[mid1]:
            high = mid1 -1
        elif key > array[mid2]:
            low = mid2 + 1
        else:
            low = mid1 + 1
            high = mid2 -1
    return -1


inputs = map(int, input().split())
arr = sorted(list(inputs))
sorted(arr)
print("Enter element to search: ")
key = int(input())
result = ternary_search(arr, key)
print(f"Element at index {result}")