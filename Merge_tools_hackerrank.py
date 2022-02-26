s = input()
s = list(s)
k = int(input())
i = 0
j = k
substring = []
while i < len(s):
    substring.append(s[i:j])
    i += k
    j += k
res_list = []
for item in range(0, len(substring)):
    modified_list = []
    for i in range(0, len(substring[item])):
        if substring[item][i] not in modified_list:
            modified_list.append(substring[item][i])
    res_list.append(modified_list)

for item in range(0, len(res_list)):
    print(''.join((res_list[item])))
