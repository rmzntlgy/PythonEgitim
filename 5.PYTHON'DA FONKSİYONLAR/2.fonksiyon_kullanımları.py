user = input("Kimsin sen!?: ")


def sayhello(name=user):
    print(f"Haa, sen miydin!? Hoşgeldin {name}!")


sayhello()


def saymyname(name=user):
    return "Merhaba " + name + "! Nerde kaldın!?"


msg = saymyname()
print(msg)


def total(num1, num2):
    return num1 + num2


a = int(input("İlk sayıyı giriniz: "))
print("Tebrikler! Kolsuz Değilsin! İkinci sayıyı gir: ")
b = int(input())
result = total(a, b)
print(f"Tuşları eskittin karşim. :) "
      f"Neyse, iki sayının toplamı: {result}")


def yashesapla(dogumyili):
    return 2021 - dogumyili


yasramazan = yashesapla(1995)
print(yasramazan)


def emeklilikhesapla(dogumyili, isim):
    yas = yashesapla(dogumyili)
    emeklilik = 65 - yas
    """
    Emeklilik hesaplanıyor burada
    input ile veri istemedim.
    kodlarda oynayın biraz.
    herşeyi hazır beklemeyin efenim :)
    """
    if emeklilik > 0:
        print(f"{isim} Emekliliğine {emeklilik} yıl kaldı")
    else:
        print(f"{isim}! Zaten emeklisin programa itlik yapmayınız.. :)")


emeklilikhesapla(1950, "Tayfun")
emeklilikhesapla(1995, "Ramazan")
