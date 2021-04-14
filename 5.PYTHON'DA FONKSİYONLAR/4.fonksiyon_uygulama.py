# 1. Gönderilen bir kelimeyi belirtildiği kadar ekranda gösteren fonksiyonu yazınız.

def yazdir(kelime, adet):
    print(kelime * adet)


yazdir("merhaba\n", 10)


# 2. Kendine gönderilen sınırsız sayıdaki parametreyi bir listeye çeviren fonksiyonu yazın.

def listeyecevir(*args):
    liste = []

    for args in args:
        liste.append(args)

    return liste


result = listeyecevir(10, 20, 30, "merhaba")
print(result)


# 3. Gönderilen 2 sayı arasındaki tüm asal sayıları bulun.


def asalsayi(sayi1, sayi2):
    for sayi in range(sayi1, sayi2 + 1):
        if sayi > 1:
            for i in range(2, sayi):
                if sayi % i == 0:
                    break
            else:
                print(sayi)


sayi1 = int(input("1. sayı: "))
sayi2 = int(input("2. sayı: "))

asalsayi(sayi1, sayi2)


# 4. Kendisine gönderilen bir sayının tam bölenlerini liste şeklinde veren fonksiyonu yazınız.

def tambolenleribul(num):
    tambolenler = []

    for i in range(2, num):
        if num % i == 0:
            tambolenler.append(i)

    return tambolenler

print(tambolenleribul(20))
