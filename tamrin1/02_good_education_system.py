n = int(input())

final_list = []

# n = 5
for _ in range(n):
    score = int(input())

    if 17 <= score <= 20:
        score = 'A'
    elif 14 <= score < 17:
        score = "B"
    elif 11 <= score < 14:
        score = "C"
    elif 8 <= score < 11:
        score = 'D'
    else:
        score = 'E'
    for idx in range(len(final_list)):
        item = final_list[idx]
        s, count = item

        if score == s:
            count += 1 
            final_list[idx] = [score, count]
            break
    else:
        final_list.append([score, 1])
print(final_list)
