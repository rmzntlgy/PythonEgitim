# dictionary yapısı
# key ve value denen ikili yapıdan oluşur

dict_isim = {35: "Selda", 67: "Müberra", 89: "Cansu", 15: "Muhammed", 35: "Ayşe"}  # key tekil(unique) olmalı
print(f"Listede 35'e atanan Selda ve Ayşe içinden Ayşe'yi aldı. dictionary yapısı gereği tekil atama olmalı."
      f"\nSonuç:    {dict_isim}")

db = {0: "", 1: "bir", 2: "iki", 3: "üç", 4: "dört", 5: "beş", 6: "altı", 7: "yedi", 8: "sekiz", 9: "dokuz"}
do = {0: "", 1: "on", 2: "yirmi", 3: "otuz", 4: "kırk", 5: "elli", 6: "altmış", 7: "yetmiş", 8: "seksen", 9: "doksan"}

sayi = input("İki basamaklı bir sayı giriniz:")
o = int(sayi[0])
b = int(sayi[1])
print(do[o], db[b])
print("Bu uygulamada 2 basamaklı bir sayı girip girilen sayıyı yazıya çevirdi.")
