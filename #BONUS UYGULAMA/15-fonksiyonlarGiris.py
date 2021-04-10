# fonksiyonlar belirli bir işin tanımlanmasının yaptığımız kod bloklarırıdır
# tekrar eden kod işlemlerinde tek sefer kod yazmamızı sağlar

# def ile belirtilir, çağrıldığı yerin üstüne yazılmalıdır

# parametre almayan ve geri döndürmeyen
def merhaba():  # def = define
    print("Merhaba algoritmaya hoş geldiniz")


merhaba()
for i in range(100):
    merhaba()

print(f'"Merhaba algoritmaya hoşgeldiniz" yazısını ekrana 100 kere yazdırdı üşenmeyenler oturup sayabilir efenim.:)')


# parametre alan fonksiyon öğreni
def hosgeldin(isim):
    print("Hoşgeldin", isim)


s = input("İsminizi giriniz:")
hosgeldin(s)


# parametre alan ve değer döndüren fonksiyonlar
def topla(a, b, c):
    return a + b + c  # return toplamı gönderir


toplam = topla(34, 23, 12)
print(toplam)

print(topla(19, 41, 67))


def kuvvet(sayi, us):
    return sayi ** us  # 3^4


sonuc = kuvvet(3, 4)
print(sonuc)
