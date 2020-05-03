
age = int(input("Enter your age: "))
if age % 2 == 0:
    result = [x for x in range(0, age + 1) if x % 2 == 0]
else:
    result = [x for x in range(0, age + 1) if x % 2 != 0]

print(result)