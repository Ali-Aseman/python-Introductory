"""
12 20 20 12 11
[['12', 2], ['20', 2], ['11', 1]]
"""
# ['12', '20', '20', '11', '12']
scores = input().split()

# [[score1, count1], [score2, count2]]
# [['20', 2], ['12', 2], ['11', 1]]
# [['20', 3], ['12', 2], ['11', 1]]
my_list = []
for item in scores:
    for idx, hasan_kachal in enumerate(my_list):
        mark, count = hasan_kachal

        if mark == item:
            count += 1
            my_list[idx] = [item, count]
            break
    else:
        my_list.append([item, 1])
print(my_list)