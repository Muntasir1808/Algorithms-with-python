def binary_search(arr, element):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < element:
            low = mid + 1
        elif arr[mid] > element:
            high = mid - 1
        elif arr[mid] == element:
            return mid
    return -1


inputs = map(int, input().split())
arr = sorted(list(inputs))
sorted(arr)
print("Enter element to search: ")
key = int(input())
result = binary_search(arr, key)
print(f"Element at index {result}")
