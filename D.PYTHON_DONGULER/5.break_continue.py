name = 'Ramazan Tolgay'

for letter in name:

    if letter == 'a':
        break
    print(letter)

print("\n\n2. örnek:")

name = 'Ramazan Tolgay'

for letter in name:

    if letter == 'a':
        continue
    print(letter)

print("\n\n3. Örnek:")
x = 0

while x < 5:
    x += 1
    if x == 2:
        break
    print(x)

print("\n4. örnek 1'den 100'e kadar olan tek sayılarınn toplamı: ")

k = 0

result = 0

while k <= 100:
    k += 1
    if k % 2 == 0:
        continue
    result += k

print(f"toplam: {result}")
