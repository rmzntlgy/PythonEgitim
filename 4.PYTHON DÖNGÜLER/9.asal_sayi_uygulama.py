"""
Soru: Girilen bir sayının asal olup olmadığını bulun.
** Asal Sayı 1 ve kendisi hariç tam böleni olmayan sayılara denir.
"""

sayi = int(input("Bir sayı giriniz: "))
asalmi = True
if sayi == 1:
    print("1 sayısı 'asal' değildir. Nedeni çarpan kümesi tek elemanlıdır. :)")

for i in range(2, sayi):

    if sayi % i == 0:
        asalmi = False

        break

if asalmi:
    print("Sayı asaldır!")
else:
    print("Sayı asal değildir!")
