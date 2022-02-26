def findMinimum(left, right):
    i = j = z = 0
    min_Arr = max(max(left), max(right))
    return min_Arr


def merge_Sorting(array):
    if len(array) > 1:
        i = j = z = 0
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]

        merge_Sorting(left)
        merge_Sorting(right)
        minimum = findMinimum(left, right)
        return minimum


size = int(input())
array = list(map(int, input().strip().split()))[:size]
smallest = merge_Sorting(array)
print(smallest)
