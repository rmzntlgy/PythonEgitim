print("Alttaki örnekte bir gariplik var:")


def changename(n):
    n = "Ramazan"


name = "Tayfun"

changename(name)
print(name)

print("Aşağıdaki kodları dikkatli inceleyiniz.")


def change(n):
    n[0] = "İstanbul"


sehirler = ["Adana", "Denizli"]

change(sehirler)
print(sehirler)


def displayuser(**args):
    for key, value in args.items():
        print("{} is {}".format(key, value))


displayuser(isim="Ramazan", yas=26, sehir="Denizli")
displayuser(isim="Haluk", yas=57, sehir="Kastamonu", tel="05551112233")
displayuser(isim="Fatma", yas=30, sehir="Niğde", eposta="fatma@m.com")
