print("liste işlemleri gibi tuple da bir liste türüdür."
      "Fakat tuple içerisindeki elemanları değiştirme veya silme işlemi yapılamaz.")

kisiler = ("ramazan", "osman", "tayfun")
liste = [1, 2, 3]   #listenin 0 indeksli değeri görüldüğü üzere çıktıda değişti.
#kisiler[0] = ("hüseyin") #burada hata alırız.
liste[0] = 5
print(kisiler)
print(liste)
