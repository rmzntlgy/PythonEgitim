x = "global x"


def function():
    x = "local x"
    print(x)


function()
print(x)

"""
Fonksiyon içinde tanımlanan x local olarak sadece 
fonksiyon altında çalıştırılabilir fonksiyon içinde
print(x) yazarsak bize local x yazdıracaktır. Global
değişkenler localde çağırılabilirken; local alandaki
tanımlamalar ancak tanımlandığı fonksiyon için geçerlidir.
Aşağıdaki örnekte ise local alanda global bir değişken
getirebiliriz. Konu bu şekilde anlaşılmıştır.
"""
print("Alttaki örnekte local alandan global bir değişken ile"
      "işlem yapabileceğimizi görüyoruz.")

x = "global x"


def function():
    print(x)


function()
print(x)

print("Küçük bir uygulama yapalım:")

isim = "Tayfun"


def isimdegistir(yeni_isim):
    isim = yeni_isim
    print(isim)


isimdegistir("Ramazan")
print(isim)

print("Uygulama:")

name = "global zone"


def greeting():
    name = "Hasan"

    def hello():
        print("Hello" + name)

    hello()


greeting()
"""
Yukarıdaki örnekte hello fonksiyonu içinde biz name değişkenine
örneğin "Osman" ismini verirsek çıktıda "Hasan" değil 
"Osman" yazacaktır. Bunun nedeni local alan altında bir 
local alan daha oluşmasıdır. Bunu bir bina ve daireleri
onunda içindeki odalar gibi düşünebilirsiniz. Bina hepinizin
ama daire ailenizin, odanız da sizin. :)

"""

print("Bir başka örnek verelim:")

a = 50


def test():
    global a
    print(f"a : {a}")

    a = 100
    print(f"Changed a  to {a}")


test()
print(a)

"""
Yukarıda a değişkeninin fonksiyon altında global olarak tanımladık.
Local alanda tanımlanan bir global değişkeni yine global alanda çağırabiliriz.
İşlemlerimizde kullanabiliriz. 

"""