a_list = [1, 2]

a1 = a_list[0]
b1 = a_list[1]

print(a1, a_list[0])
print(b1, a_list[1])
a2, b2 = a_list
print(a2, b2)
print("-------------------")
print("-------------------")
a5, *b5 = [1, 2, 3]
print(a5, b5)

a6, *b6, c6 = [1, 2, 3, 4]
print(a6, b6, c6)
