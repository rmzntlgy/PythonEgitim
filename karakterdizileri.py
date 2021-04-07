isim = "Ramazan"
soyisim = "TOLGAY"
yas = 26

print("Merhaba, Ben "+isim+soyisim+", yaşım "+ str(yas) )

#isim değişkenine atadığımız Ramazan ifadesi 7 indeksli bir karakter dizisidir.
#karakter dizilerinin ilk indeks değeri 0 ile başlar. Aşağıdaki örnekte 0. indeks değeri R olarak karşımıza çıkar.

print("İsim değişkeni 0 indeksli değeri=",isim[0])
print("İsim değişkeni 1 indeksli değeri=",isim[1])
print("İsim değişkeni 2 indeksli değeri=",isim[2])
print("İsim değişkeni 3 indeksli değeri=",isim[3])
print("İsim değişkeni 4 indeksli değeri=",isim[4])
print("İsim değişkeni 5 indeksli değeri=",isim[5])
print("İsim değişkeni 6 indeksli değeri=",isim[6])

print("isim değişkenin -1 indeksli değeri son karakteri verir;",isim[-1])

print("len komutu ile karakter dizisinde kaç karakter olduğunu buluruz.",
      "\nİsim değişkenimizin karakter sayısı:",len(isim))
print("İndeks ile belirlediğimiz bir aralıkta işlem yaparken \":\" işaretini kullanırız. Örnek;")


print("Bu örnekte 2 ve 5 indeskli karakterleri yazdırdık. Sonuç;",isim[2:5])

print("Bu örnekte 1'den başlayıp 2 karakter atalayarak 6. indekse kadar yazdırma işlemi yaptık. Sonuç;",
      isim[1::2])

#farkettiğiniz üzere 2. değeri yazmadık bu da karakter dizisinin sonuna kadar gitmesini sağladı.
"""Bu ders burada bitti. Sonraki ders \"string\" formatlama"""