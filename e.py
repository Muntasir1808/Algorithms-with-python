def merge_sort(my_list):
    if len(my_list) > 1:
        high = len(my_list) - 1
        mid1 = high // 3
        mid2 = 2 * mid1
        left_list = my_list[:mid1]
        mid_list = my_list[mid1:mid2]
        right_list = my_list[mid2:high]
        merge_sort(left_list)
        merge_sort(mid_list)
        merge_sort(right_list)
        i = j = m = k = 0
        while i < len(left_list) and j < len(right_list) and m < len(mid_list):
            if left_list[i] <= right_list[j] and left_list[i] <= mid_list[m]:
                my_list[k] = left_list[i]
                i += 1
                k += 1
            elif right_list[j] <= left_list[i] and right_list[j] <= mid_list[m]:
                my_list[k] = right_list[j]
                j += 1
                k += 1
            else:
                my_list[k] = mid_list[m]
                m += 1
                k += 1
        while i < len(left_list):
            my_list[k] = left_list[i]
            i += 1
            k += 1
        while j < len(right_list):
            my_list[k] = right_list[j]
            j += 1
            k += 1
        while m < len(mid_list):
            my_list[k] = mid_list[m]
            m += 1
            k += 1


a = list(map(int, input().split()))
merge_sort(a)
print(a)
