n = int(input())

final_list = []
"""
4
ali 20 19 18
asghar 20 20 20
akbar 19 20 15
hassan 20 20 19 18
"""
for _ in range(n):
    items = input().split()
    name = items[0]

    sum_scores = 0
    for idx in range(1, len(items)):
        sum_scores += int(items[idx])
    final_list.append([name, sum_scores / (len(items) - 1)])

failed_list = []
for item in final_list:
    name, avg = item
    if avg < 12:
        failed_list.append(item)
print(failed_list)
