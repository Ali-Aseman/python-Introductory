"""
در خط اول ابتدا تعداد نمرات دانش آ«وزان را از کاربر دریافت کنید.
در n خط بعدی کاربر نمرات دانش آموزان را برای شما وارد میکند.

برای حفظ آبروی مدرسه از شما خواسته شده است تا برنامه ای بنویسید که نمرات کمتر از ۱۰ را از لیست نمرات حذف نماید.
"""
n = int(input("enter the number : "))

my_list = []

for _ in range(n):
    py = int(input())
    if py > 20 or py < 0:
        print("wrong input")
    else:
        my_list.append(py)
        
nomarat_list = []

for py in my_list:
    if py >=10:
        nomarat_list.append(py)

print(f"nomarat : {nomarat_list}")    
