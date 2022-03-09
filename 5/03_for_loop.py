fruits = ["apple", "orange", "banana"]

print(fruits[0])
print(fruits[1])
print(fruits[2])

print("----------------")
for item in fruits:
    print(item) 
    if item == "apple":
        continue  

    print(item)

print("----------------")
# fruits = ["apple", "orange", "banana"]
for item in fruits:
    print(item)

    if item == "apple":
        break

    print(item)
