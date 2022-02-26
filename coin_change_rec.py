def recursive_coin_change(n, v, i):
    if n > 0:
        if v[i] <= n:
            print(v[i])
            return 1 + recursive_coin_change(n-v[i], v, i)
        else:
            return recursive_coin_change(n, v, i+1)
    else:
        return 0


notes = list(map(int, input().split()))
change = int(input())
res = recursive_coin_change(change, notes, 0)
print(res)
