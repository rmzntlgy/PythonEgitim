# Set = kume yapısı
kume = {"Ali", "Deniz", "Ayşe", "Fatma", "Hayriye", "Bilge", "Ali", "Deniz"}
print(kume)
print(len(kume))
kume.add("Muhammed")
print(kume)

a = {1, 5, 6, 7, 0, 2, 3}
b = {4, 8, 9, 2, 1, 0, 3}

d = a.union(b)  # aUb birleşim
print(d)

c = a.intersection(b)  # keşisim
print(c)

e = a.difference(b)  # fark a-b
print(e)

dizi = [9, 0, 0, 1, 2, 3, 5, 6, 6, 0, 9]
print(dizi)

kume1 = set(dizi)  # dizi sete çevrilir, tekrar eden elemanlar bir kere yazılır
print(kume1)

skume = set("Algoritma dersi şiir gibi anlatılıyor")
print(skume)
