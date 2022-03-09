# جمع کل المان های داخل مای لیست

#  برای لیست خطی
my_list = [11, 12, 13, 14]
# sum_upto_now = 0
# for item in my_list:
#     sum_upto_now += item
# ----------------------------

my_list = [
    [1, 2, 3],
    [4, 5, 6]
]
# s = 0
b = 0
for item in my_list:
    s = 0
    for a in item:
        s += a
    print(f"s: {s}")
    b += s
print(f"sum: {b}")
print(sum_upto_now)
