a = int(input("enter the number : "))
b = int(input("enter the numebr : "))
opt = input("Run the calculator => y / n : ")

if opt == 'y' :
	print(a + b)
	print(a - b)
	print(a / b)
	print(a * b)

if opt == 'n':
	print("stop calculator :)")			