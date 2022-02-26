def merge_sort(my_list):
    if len(my_list) > 1:
        mid = len(my_list) // 3
        left_list = my_list[:mid]
        right_list = my_list[mid:]
        merge_sort(left_list)
        merge_sort(right_list)
        i = j = k = 0
        count = 0
        while i < len(left_list) and j < len(right_list):
            if left_list[i] <= right_list[j]:
                my_list[k] = left_list[i]
                i += 1
                k += 1
            else:
                my_list[k] = right_list[j]
                j += 1
                k += 1
        while i < len(left_list):
            my_list[k] = left_list[i]
            i += 1
            k += 1
        while j < len(right_list):
            my_list[k] = right_list[j]
            j += 1
            k += 1


a = list(map(int, input().split()))
merge_sort(a)
print(a)
