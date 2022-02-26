def printMaxActivities(activities, s, f):
    n = len(f)
    print(s)
    print(f)
    schedule = []
    print("The following activities are selected")
    i = 0
    # print(i)
    schedule.append(activities[i])

    for j in range(n):
        print(j)
        if s[j] >= f[i]:
            schedule.append(activities[j])
            i = j
            print(f"is {i}")
    return schedule


length = int(input("Enter length: "))
print("Input start time and finish time of activities:")
activities = []
for item in range(0, length):
    time = list(map(int, input().split()))
    activities.append(time)
activities.sort(key=lambda x: x[1])
print(activities)
start = []
finish = []
for items in range(0, len(activities)):
    finish.append(activities[items][1])
    start.append(activities[items][0])
res = printMaxActivities(activities, start, finish)
print(res)
