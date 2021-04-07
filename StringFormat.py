isim = "Ramazan"
soyisim = "TOLGAY"

print("Merhaba, ben {} {}".format(isim, soyisim))
#Aşağıdaki örnekte indeks değerleri ile atama yaptık ve soyisimi önce yazdırdık.
print("Merhaba, ben {1} {0}".format(isim, soyisim))
#Aşağıdaki örnekte ise format içerisinde değer ataması yaparak soyisimi öne aldık.
print("Merhaba, ben {s} {i}".format(i=isim, s=soyisim))