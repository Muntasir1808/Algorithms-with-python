def find_max_cross_sub(a, low, mid, high):
    summation = 0
    left_sum = float('-inf')
    for item in range(mid, low - 1, -1):
        summation = summation + a[item]
        if summation > left_sum:
            left_sum = summation
    summation = 0
    right_sum = float('-inf')
    for item in range(mid + 1, high + 1):
        summation = summation + a[item]
        if summation > right_sum:
            right_sum = summation
    return max(left_sum + right_sum, left_sum, right_sum)


def find_max_sub(array, low, high):
    if low == high:
        return array[low]
    mid = (low + high) // 2
    return max(find_max_sub(array, low, mid),
               find_max_sub(array, mid + 1, high),
               find_max_cross_sub(array, low, mid, high))


arr = list(map(int, input().split()))
length = len(arr)
res = find_max_sub(arr, 0, length-1)
print(res)

