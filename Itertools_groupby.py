import itertools

data_set = [100, 80, 90, 80, 80, 90, 70, 100]
keys = []
groups = []
# sorted_data = sorted(data_set)
for k, v in itertools.groupby(data_set):
    keys.append(k)
    groups.append(list(v))
print('keys: ', keys)
print('Groups: ', groups)

# count per group
for items in groups:
    print(len(items))