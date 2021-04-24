"""
Bu kodlarda eksikler var daha sonra aynı konuya dönüş yap!

"""


def not_hesapla(satir):
    satir = satir[:-1]
    liste = satir.split(":")

    ogrenciadi = liste[0]
    notlar = liste[1].split(",")

    not1 = int(notlar[0])
    not2 = int(notlar[1])
    not3 = int(notlar[2])

    ortalama = (not1 + not2 + not3) / 3

    if 90 <= ortalama <= 100:
        harf = "AA"
    elif 85 <= ortalama <= 89:
        harf = "BA"
    elif ortalama >= 65:
        harf = "CC"
    else:
        harf = "FF"
    return ogrenciadi + ":" + harf + "\n"


def ortalamalari_oku():
    with open("sinav_notlari.txt", "r", encoding="utf-8") as file:
        for satir in file:
            print(not_hesapla(satir))


def not_gir():
    ad = input('Öğrendi Adı: ')
    soyad = input('Öğrendi soyadı: ')
    not1 = input('Not 1: ')
    not2 = input('Not 2: ')
    not3 = input('Not 3: ')

    with open("sinav_notlari.txt", "a", encoding="utf-8") as file:
        file.write(ad + " " + soyad + ":" + not1 + "," + not2 + "," + not3 + "\n")


def notlari_kaydet():
    pass


while True:
    islem = input('1- Notları Oku\n2- Not Gir\n3- Notları kaydet\n4- Çıkış\n')

    if islem == '1':
        ortalamalari_oku()
    elif islem == '2':
        not_gir()
    elif islem == '3':
        notlari_kaydet()
    else:
        break
