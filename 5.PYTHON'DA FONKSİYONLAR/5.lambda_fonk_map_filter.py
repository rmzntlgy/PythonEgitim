# def square(num): return num ** 2

numbers = [1, 2, 3, 4, 7]

# map(square, numbers)
# result = list(map(square, numbers))
result = list(map(lambda num: num ** 2, numbers))
print(result)

# for item in map(square, numbers):
#    print(item)


square = lambda say: say ** 2

sayilar = [1, 2, 3, 7, 9]

sonuc = square(3)
print(f"ikinci örnek sonucu: {sonuc}")

print("Diğer örnek:")

li = [2, 5, 3, 6, 8]


def check_even(num): return num % 2 == 0


d_sonuc = list(filter(check_even, li))
print(d_sonuc)

print("lambda ile hazırlanmış kodlar:")

li = [2, 5, 3, 6, 8]


def check_even(num): return num % 2 == 0


d_sonuc = list(filter(lambda num: num%2==0, li))
print(d_sonuc)