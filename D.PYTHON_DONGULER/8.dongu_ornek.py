import random

"""
1-100 arasında rastgele üretilecek bir sayıyı aşağı yukarı ifadeleri ile bulmaya çalışın.

   **"random modülü" için "python random" şeklinde arama yapın.
   **100 üzerinden puanlama yapın. Her yanlış puan  20 puan götürsün.
   **Hak bilgisini kullanıcıdan alın ve her soru belirtilen can sayısı üzerinden hesaplansın.
"""

sayi = random.randint(1, 100)
can = int(input("Kaç hak tanımlansın?\n HAK: "))
hak = can
sayac = 0
while hak > 0:

    hak -= 1
    sayac += 1
    tahmin = int(input('tahmin: '))
    if sayi == tahmin:
        print(f'Tebrikler {sayac}. seferde bildiniz. Puanınız: {100 - (100 / can) * (sayac - 1)}')
        break

    elif sayi > tahmin:
        print("Yukarı")
    else:
        print("Aşağı")

    if hak == 0:
        print(f"Hakkınız bitti. Tutulan sayi: {sayi}")
