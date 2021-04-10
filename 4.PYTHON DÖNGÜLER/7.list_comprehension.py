numbers = []

for x in range(10):
    numbers.append(x)

print(numbers)

numbers = [x for x in range(10)]
print(numbers)

for x in range(10):
    print(x ** 2)

numbers = [x ** 2 for x in range(10)]
print(numbers)

numbers = [x * x for x in range(10) if x % 3 == 0]
print(numbers)

mystring = "Hello!"

mylist = []

for letter in mystring:
    mylist.append(letter)

print(mylist)

mylist = [letter for letter in mystring]
print(mylist)

years = [1999, 1965, 2001, 1989]

ages = [2021 - years for years in years]
print(ages)

results = [x if x % 2 == 0 else 'TEK' for x in range(1, 10)]
print(results)

result = []
for x in range(3):
    for y in range(3):
        result.append((x, y))

print(result)

numbers = [(x, y) for x in range(3) for y in range(3)]
print(numbers)
