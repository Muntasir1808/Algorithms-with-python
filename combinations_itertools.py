from itertools import combinations
string, n = input().split()
n = int(n)

for items in range(1, n+1):
    combination_list = []
    combination_list = list(combinations(sorted(string), items))
    for i in range(0, len(combination_list)):
        print(''.join(combination_list[i]))
