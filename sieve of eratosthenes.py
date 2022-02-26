n = int(input())
prime = []
p2 = []
q = 3
for i in range(n+1):
    prime.append(i)
prime[0] = 0
prime[1] = 0
p = 2
while p ** 2 <= n:
    if p != 0:
        for item in range(p ** 2, n + 1, p):
            prime[item] = 0
    p += 1
print(prime)
for item in range(len(prime)):
    if prime[item] != 0:
        p2.append(prime[item])

numbers = [2, 3, 4, 5, 6, 7]
a = [[] for i in range(q+1)]
b = [[] for i in range(q+1)]
answers = []
a[0] = numbers
for i in range(q):
    while a[i]:
        plate = a[i].pop()
        if plate % p2[i] == 0:
            b[i+1].append(plate)
        else:
            a[i+1].append(plate)
for i in range(q+1):
    while b[i]:
        answers.append(b[i].pop())
for i in range(q+1):
    while a[i]:
        answers.append(a[i].pop())
print(*answers)