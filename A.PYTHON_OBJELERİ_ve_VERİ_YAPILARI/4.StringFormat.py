isim = "Ramazan"
soyisim = "TOLGAY"

print("Merhaba, ben {} {}".format(isim, soyisim))
#Aşağıdaki örnekte indeks değerleri ile atama yaptık ve soyisimi önce yazdırdık.
print("Merhaba, ben {1} {0}".format(isim, soyisim))
#Aşağıdaki örnekte ise format içerisinde değer ataması yaparak soyisimi öne aldık.
print("Merhaba, ben {s} {i}".format(i=isim, s=soyisim))
yas = 26
print("Merhaba, ben {s} {i}, {y} yaşındayım.".format(i=isim, s=soyisim, y=yas))

bolum= 13/7
print("SONUÇ:{}".format(bolum))

print("SONUÇ:{b:2.4}".format(b=bolum))

print(f"Merhaba benim adım {isim} ve {yas} yaşındayım.") #f ile yazdırma işlemi şekildeki gibidir. En başa f yazdık.