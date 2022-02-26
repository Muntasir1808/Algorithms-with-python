def binary_search(array, low, high, element):
    if low <= high:
        mid = (low + high)/2
        if arr[mid] > element:
            return binary_search(array, low, mid-1, element)
        elif arr[mid] < element:
            return binary_search(array, mid+1, high, element)
        elif arr[mid] == element:
            return mid
    return -1


inputs = map(int, input().split())
arr = sorted(list(inputs))
sorted(arr)
print("Enter element to search: ")
key = int(input())
result = binary_search(arr, 0, len(arr)-1, key)
print(f"Element at index {result}")