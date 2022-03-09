a , rotate_count = input().split()
b = input().split()

rotate_count = int(rotate_count) % int(a)
print(b[rotate_count:] + b[:rotate_count])