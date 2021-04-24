sayilar = [1, 3, 5, 7, 9, 12, 19, 21]
# 1: sayilar listesini while ile ekrana yazdırın.

d = 0
while d < len(sayilar):
    print(sayilar[d])
    d += 1

# 2: Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm tek sayıları ekrana yazdırın.
baslangic = int(input('Başlangıç sayısı: '))
bitis = int(input('Bitiş sayısı: '))

i = baslangic

while i < bitis:
    i += 1
    if i % 2 == 1:
        print(i)

# 3: 1-100 arasındaki sayıları azalan şekilde yazdırın.
a = 100

while a > 0:
    print(a)
    a -= 1

# 4: Kullanıcıdan gelen 5 sayıyı ekranda sıralı bir şekilde yazdırın.
sayilar = []

b = 0

while b < 5:
    sayi = int(input('Sayi giriniz: '))
    sayilar.append(sayi)
    b += 1

sayilar.sort()

print(sayilar)

# 5: Kullanıcadan alacağınız sınırsız ürün bilgisini urunler listesi içinde saklayın.
#       **ürün sayısını kullanıcıuya sorun.
#       **dictionary listesi yapısı (name, price) şeklinde oluşsun.
#       **ürün ekleme işlemi bittiğinde ürünleri ekranda while ile listeleyin.
urunler = []

adet = int(input('Kaç adet ürün eklemek istiyorunuz? :'))

c = 0

while c < adet:
    urun_ismi = input('Ürün İsmi: ')

    urun_fiyati = int(input('Ürün fiyatı: '))
    urunler.append({
        'urun_ismi': urun_ismi,
        'urun_fiyati': urun_fiyati
    })
    c += 1

for urun in urunler:
    print(f"Ürün adı: {urun['urun_ismi']} Ürün fiyatı: {urun['urun_fiyati']}")
