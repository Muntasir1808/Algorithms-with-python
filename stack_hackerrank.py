def waiter(number, q):
    # Write your code here
    prime = []
    p2 = []
    for i in range(10000):
        prime.append(i)
    prime[0] = 0
    prime[1] = 0
    p = 2
    while p ** 2 <= 10000:
        if p != 0:
            for item in range(p ** 2, n + 1, p):
                prime[item] = 0
    p += 1

    for item in range(len(prime)):
        if prime[item] != 0:
            p2.append(prime[item])

    a = [[] for i in range(q + 1)]
    b = [[] for i in range(q + 1)]
    answers = []
    a[0] = number
    for i in range(q):
        while a[i]:
            plate = a[i].pop()
            if plate % p2[i] == 0:
                b[i + 1].append(plate)
            else:
                a[i + 1].append(plate)
    for i in range(q + 1):
        while b[i]:
            answers.append(b[i].pop())
    for i in range(q + 1):
        while a[i]:
            answers.append(a[i].pop())
    return answers
