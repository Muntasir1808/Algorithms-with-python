def partition(arr, start, end):
    pivot = arr[end]
    p_index = start
    for item in range(start, end):
        if arr[item] < pivot:
            arr[item], arr[p_index] = arr[p_index], arr[item]
            p_index = p_index + 1
    arr[p_index], arr[end] = arr[end], arr[p_index]
    return p_index


def quick_sort(array, start, end):
    if len(array) == 1:
        return array
    if start < end:
        p_index = partition(array, start, end)
        quick_sort(array, start, p_index - 1)
        quick_sort(array, p_index + 1, end)


n = int(input())
a = list(map(int, input().split()))
quick_sort(a, 0, len(a)-1)
print(*a)
