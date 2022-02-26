a = int(input())
rating = []
for item in range(0, a):
    marks = int(input())
    rating.append(marks)
candies = 0
candies_list = [1] * len(rating)
total_candies = 0
# for item in range(0, len(rating)):
#     candies_list.append(1)
#     total_candies += 1
for item in range(1, len(rating)):
    if rating[item] > rating[item-1] and candies_list[item] <= candies_list[item-1]:
        candies_list[item] = candies_list[item-1]+1
        total_candies += 1

for i in range(len(rating)-1, 0, -1):
    if rating[i-1] > rating[i] and candies_list[i-1] <= candies_list[i]:
        candies_list[i-1] = candies_list[i]+1
# print(candies_list)
print(sum(candies_list))
