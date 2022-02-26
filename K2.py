a = list(map(int, input().split()))
max_so_far = a[0]
max_ending_here = a[0]
s_index = 0
e_index = 0
s_index_ending_here = 0
for item in range(0, len(a)):
    max_ending_here = max_ending_here + a[item]
    if max_ending_here < a[item]:
        max_ending_here = a[item]
        s_index_ending_here = item
    if max_ending_here > max_so_far:
        max_so_far = max_ending_here
        e_index = item
        s_index = s_index_ending_here
print(max_so_far)
