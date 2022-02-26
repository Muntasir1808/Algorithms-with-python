def poisonousPlants(p):
    max_days = 0
    s = []
    for i in range(len(p)):
        alive = 0
        while s and p[i] <= s[-1][0]:
            alive = max(alive, s.pop()[1])
        if s:
            alive = alive + 1
            s.append([p[i], alive])
        elif not s:
            alive = 0
            s.append([p[i], alive])

        max_days = max(alive, max_days)

    return max_days


# n = int(input().strip())
p = list(map(int, input().rstrip().split()))
result = poisonousPlants(p)
print(result)
