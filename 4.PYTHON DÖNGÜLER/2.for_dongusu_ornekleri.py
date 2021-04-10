sayilar = [1, 3, 5, 7, 9, 12, 19, 21]
# 1- sayilar listesindeki hangi sayılar 3'ün katıdır?

for sayi in sayilar:
    if sayi % 3 == 0:
        print(f"Listedeki üçün katı olan sayılar;{sayi}")
print("\n")
# 2- sayilar listesinde sayıların toplamı kaçtır?

toplam = 0
for sayi2 in sayilar:
    toplam += sayi2
print(f"Listedeki sayıların toplamı;{toplam}")
# 3- sayilar listesindeki tek sayıların karesini alınız.
print("\n")
for sayi1 in sayilar:
    if sayi1 % 2 == 1:
        print(f"Listedeki tek sayıların karesi; {sayi1 ** 2}")

sehirler = ['kocaeli', 'istanbul', 'ankara', 'izmir', 'rize']

# 4- Şehirlerden hangileri en fazla 5 karakterlidir?
print("\n")
for sehir in sehirler:
    if len(sehir) <= 5:
        print(f"En fazla beş karakterli şehir isimleri: {sehir}")

urunler = [

    {'name': 'samsung s6', 'price': '3000'},
    {'name': 'samsung s7', 'price': '4000'},
    {'name': 'samsung s8', 'price': '5000'},
    {'name': 'samsung s9', 'price': '6000'},
    {'name': 'samsung s10', 'price': '7000'},
]

# 5- Ürünlerin fiyatları toplamı nedir?
print("\n")
toplam = 0
for urun in urunler:
    fiyat = int(urun['price'])
    toplam += fiyat
print(f"Ürünlerin fiyatlarının toplamı {toplam} TL\n")


# 6- Ürünlerden fiyatı en fazla 5000 olan ürünleri gösteriniz.

for urun in urunler:
    if int(urun['price']) <= 5000:
        print(f"Fiyatı en fazla 5000 tl olan ürünler; {urun['name']}")
