my_list = [1, 2, 4, 0, 5 , 7, 0, 9]

for item in my_list:
    if item == 0:
        my_list.remove(item)
        my_list.append(item)

print(my_list)
