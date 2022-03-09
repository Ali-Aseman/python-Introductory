"""
3
5
11
12
"""
number_score = int(input("Enter the number : "))

my_list = []

for idx in range(number_score):
    py = int(input())
    
    if py > 20 or py < 0:
        print("wrong number")
    else:
        my_list.append(py)


my_list_copy = my_list.copy()

for item in my_list_copy:
    if item < 10:
        my_list.remove(item)    
print(my_list)
















