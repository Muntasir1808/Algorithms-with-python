def job_sequencing(sequence_list, no_jobs):
    sequence_list.sort(key=lambda x: int(x[2]), reverse=True)
    print(sequence_list)
    table = [-1 for x in range(no_jobs)]
    job = [False for x in range(no_jobs)]
    print(table)
    for items in range(0, len(sequence_list)):
        deadline = int(sequence_list[items][1])
        if table[deadline - 1] == -1 and job[deadline - 1] is False:
            table[deadline - 1] = sequence_list[items][0]
            job[deadline - 1] = True
            print(f"1st one done {table[deadline - 1]}")
        else:
            for item in range(deadline-1, -1, -1):
                index = deadline-1
                print(f" inside else {index}")
                print(f"job index = {job[index - 1]}")
                if index-1 >= 0 and table[index - 1] == -1 and job[index - 1] is False:
                    print(f"deadline = {deadline}")
                    print(f"item = {index}")
                    print(f"inside {table[index-1]}")
                    table[index - 1] = sequence_list[index][0]
                    print(f"else part is executing for {sequence_list[items][0]}")
                    job[index - 1] = True
                    break
    # res = []
    # for items in range(0, len(table)):
    #     if table[items] != -1:
    #         res.append(table[items])
    res = []
    [res.append(x) for x in table if x != -1]

    print(res)
    print(table)


no_of_jobs = int(input())
sequences = []
for _ in range(0, no_of_jobs):
    sequences.append(list(input().split()))
job_sequencing(sequences, no_of_jobs)

