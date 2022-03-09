n = int(input())

dict1 = {}

for i in range(n):
	score = input().split()
	name = score.pop(0)
	s = sum(list(map(int, score)))
	avg = s / len(score)
	dict1[name] = avg
print(dict1)	