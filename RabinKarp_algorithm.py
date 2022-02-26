d = 256


def search(pat, txt, q):
    M = len(pat)
    N = len(txt)
    i = 0
    j = 0
    p = 0
    t = 0
    h = 1

    h = (d ** (M-1)) % q
    print(h)

    for i in range(M):
        p = (d * p + ord(pat[i])) % q
        # print(ord(pat[i]))
        print(p)
        t = (d * t + ord(txt[i])) % q
        print(t)
    for i in range(N - M + 1):
        if p == t:
            for j in range(M):
                if txt[i + j] != pat[j]:
                    break
                else:
                    j += 1

            if j == M:
                print("Pattern found at index " + str(i))

        if i < N - M:
            print(f"inside {t}")
            t = (d * (t - ord(txt[i]) * h) + ord(txt[i + M])) % q
            print(f"{d} * {t} - {ord(txt[i])} * {h} + {ord(txt[i + M])} % {q}")
            if t < 0:
                t = t + q


txt = "ABDAB"
pat = "AB"
q = 13
search(pat, txt, q)
