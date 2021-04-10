print("Aşağıdaki örnekte sıfır indeksten başlayıp 9. indekse kadar range ile 10 elemanlı bir dizi oluşturduk.")
for item in range(10):
    print(item)
print("10 ile başlatıp 20 ye kadar olan sayı dizisi: ")

for sayilar in range(10, 20):
    print(sayilar)
print("Alttaki örnekte sıfırdan başlayıp ikişer olarak 98 e kadar yazdırdık. 3. parametre artış miktarını belirtir!")
for sayi_liste in range(0, 100, 2):
    print(sayi_liste)

print(f"Bu da liste şekilde yazdırma: {list(range(10, 20))}")

print("'enumerate metodu kullanımı aşağıdaki gibidir.")
selamlama = "Merhaba!"

for yazi in enumerate(selamlama):
    print(yazi)

selamla = "Merhaba!"
for indeks, yazi in enumerate(selamla):
    print(f'indeks: {indeks} yazi: {yazi}')

list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c', 'd', 'e']

print(f"Zip metodu ile bir liste birleştirme "
      f"yapalım bu da son örnek: {list(zip(list1, list2))}")

print("Başka bir uygulama da bu şekilde:")
for item in list(zip(list1, list2)):
    print(item)
