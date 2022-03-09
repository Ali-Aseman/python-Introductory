nomre = int(input())

final_list = []
for _ in range(nomre):
    items = input().split()
    name = items[0]

    ali = 0
    for idx in range(1, len(items)):
        ali += int(items[idx])
    final_list.append([name, ali / (len(items) - 1)])

list_end = []
for item in final_list:
    name, avg = item
    if avg > 10:
        list_end.append(item)
print(list_end)
