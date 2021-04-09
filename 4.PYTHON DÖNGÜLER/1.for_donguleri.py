"""
Bu derste for döngüleri ile işlem yapmayı göreceğiz.

"""
print("Evet aşağıdaki örnekte olduğu gibi liste içerisindeki elemanları,"
      "for döngüsü içerisinde tek tek yazdırdı. Her bir eleman için döngü çalışmaya devam etti.")
liste = [1, 2, 3, 4, 5]

for sayi in liste:
    print(sayi)

print("\nAlttaki örnekte ise isimler listesindeki her kullanıcı için for döngüsü devam etti.")

isimler = ['Ali', 'Veli', 'Ramazan']

for kullanicilar in isimler:
    print(kullanicilar)

print("Peki ya bir değişkene 'string dizisi' tanımlayıp bunu for döngüsü içinde kullanırsak ne olur?"
      "\nÖrneği inceleyiniz.")

kullanici_id = 'rmzntlgy'

for kullanici in kullanici_id:
    print(kullanici)

print(f"Evet yukarıdaki örnekte string dizisi olarak for döngüsü oluşturduk.\n"
      f"{kullanici_id} kullanıcı adının her index değeri için for döngüsü devam etti.\n"
      f"Bu arada {kullanici_id} kullanıcı adının index sayısı;{len(kullanici_id)}")

print("\n\n\nEvet Aşağıdaki tuple listesi örneklerini dikkatlice inceleyiniz.\n")

tuple_list = (1, 2, 3, 4, 5, 6)

for t in tuple_list:
    print(t)

print("\nBaşka bir örnek;\n")

tuple_list_1 = [(1, 2), (3, 4), (5, 6)]

for a in tuple_list_1:
    print(a)

print("\nAşağıdaki örneğin çıktısını ve kodlarını inceleyerek konuyu kavramaya çalışınız.")

for (a, b) in tuple_list_1:
    print(a)

print("Aşağıda 2'li değer olarak yazdırdık;\n")
for (a, b) in tuple_list_1:
    print(a, b)

print("Dictionary listesi ile for döngüsü örneğini inceleyiniz:\n")

users = {'user1': 1, 'user2': 2, 'user3': 3}

for ka in users:
    print(ka)

print("\nAha! Kullanıcılara karşılık gelen değerler yok! \nBu sorunu aşamanın yolu aşağıdaki örnekte var."
      "\nEvet sözlükler değerleri farklı alanda tuttukları için anahtarlara karşılık gelen değerlere"
      " '.items' metodu ile ulaşıyoruz.\n")

for (anahtar, deger) in users.items():  # anahtar=key, değer=value
    print(anahtar, deger)
