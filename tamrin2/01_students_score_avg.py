"""
در خط اول از کاربر تعداد نمرات دانش آموزان را دریافت کنید.
سپس در n خط بعدی نمرات دانش آموزان را از کاربر دریافت کنید و میانگین نمرات رو در خروجی نمایش دهید.
"""

n = int(input("enter the number : "))

my_list = []

for _ in range(n):
    py = int(input())
    if py > 20 or py < 0:
        print("wrong number")
    else:
        my_list.append(py)    

score_name = 0

score_name = sum(my_list)

print(f"miyangin : {score_name / n}")