alpha = "abcdefghijklmnopqrstuvwxyz"

n = int(input())
for idx in range(n - 1):
    right = "-".join(alpha[n - idx - 1: n])
    left = right[::-1]
    spaces = "".join([" "] * (((n - 1 - (idx + 1)) * 2)))
    print(spaces + left + right[1:])
