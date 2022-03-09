def f(x, y):
    return x ** 2 + y ** 2


print(f(1, 2))
print(f(2, 2))

l1 = ["1", "2", "3", "4"]


def multiple_two(number):
    return int(number) * 2
    # return None


print(list(map(int, l1)))
print(tuple(map(multiple_two, l1)))
print(set(map(multiple_two, l1)))
print(map(multiple_two, l1))

for item in map(multiple_two, l1):
    print(item)

# print(int("12"))
#
# # list([1, 2 ,3 ])
# t = ((1, 2), (3, 4))
#
# print(dict(((1, 2), (3, 4))))
