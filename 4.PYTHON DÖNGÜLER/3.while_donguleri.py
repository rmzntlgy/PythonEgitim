# Sıfırdan başlayıp 100'e kadar olan sayıları while ile yazdırma örneği.
x = 0
print("Sıfırdan başlayıp 100'e kadar olan sayıları while ile yazdırma örneği.")
while x <= 100:
    print(x)
    x += 1
print("Bitti..")

print("Sıfırdan başlayıp 100'e kadar olan sayıları ikişer olarak while ile yazdırma örneği.")
x = 1
while x <= 100:
    if x % 2 == 0:
        print(x)
    x += 1
print("Bitti..")


print("Kullanıcıdan veri alarak while döngüsü oluşturma (Boş değer girdikçe döngü devam edecektir!);")

rastgele = ""
while not rastgele.strip():
    rastgele = input("rastgele bir ifade giriniz:")

