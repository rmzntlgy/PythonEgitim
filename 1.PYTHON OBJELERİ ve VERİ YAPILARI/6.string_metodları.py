mesaj = "Merhaba ben Ramazan TOLGAY."
print("Upper Metodu; Bu metod ile harfleri büyük harfe çeviriyoruz.\n")
print(f"1)Bu örnekte mesajımızın bütün harflerini büyük olarak yazdıracağız: {mesaj.upper()}")
print("2)Yukarıdaki mesajı yazdırmanın başka bir yolu da bu şekilde;", mesaj.upper())
print("\n3)Açıklama satırı kullanıp kodları açıklayabilirdim fakat çıktıda hepsini görmeniz için tek tek yazıyorum.")
print("*Evet 'upper' metodu kullanarak bir karakter dizisindeki harflerin hepsini büyük harf olarak çevirdik. ")


print("\nLower Metodu; Bu metod ile harfleri küçük harflere çeviriyoruz.")
print(f"1)Bu örnekte mesajımızın bütün harflerini küçük olarak yazdıracağız: {mesaj.lower()}")
print("2)Yukarıdaki mesajı yazdırmanın başka bir yolu da bu şekilde;", mesaj.lower())


print("Title Metodu; bu metod ile her kelimenin baş harfini büyük yapıyoruz.")
print(f"1)Bu örnekte mesajımızdaki her kelimenin başındaki harfi büyük olarak yazdıracağız: {mesaj.title()}")
print("2)Yukarıdaki mesajı yazdırmanın başka bir yolu da bu şekilde;", mesaj.title())


print("Capitalize Metodu; Bu metot ile yazdırdığınız çıktının ilk harfini büyük yazıp geri kalanını küçük yazar.")
print(f"Mesajımızı bu metodla yazdırınca çıktı tam olarak bu şekilde verir;\n{mesaj.capitalize()}")

print(f"Strip Metodu örneği;\n{mesaj.strip()}")


print(f"split metodu örneği;\n{mesaj.split()}")
print(f"split metodu parametreli örnek; {mesaj.split('.')}")


mesajs = mesaj.split()
mesaj1 = ' '.join(mesajs)
mesaj2 = '*'.join(mesajs)
print(f"join metodu; {mesaj1}")
print("join metodu biraz kafa karıştırdı sanırım."
      "\nBu örnekte split metodu ile her iki boşluk arasındaki ifadeleri karakter dizesi haline getirdik."
      "\nSonrasında join metodu ile aralara boşluk koyarak tekrar kelimeyi birleştirdik."
      "\nİsterseniz araya yıldız koyarak tekrar birleştirme yapalım.")
print(f"Yıldız koyarak birleştirilmiş hali;{mesaj2}")


print(f"Find metodu örneği:{mesaj.find('Ramazan')}")
print("Find metodunda veren 12 değeri. arattığımız sonucu kelimenin başladığı indeks değerini verir.")
print(f"Haluk kelimesini arattığımızdaki sonuç; {mesaj.find('Haluk')}")
print("-1 değeri arattığımız değerin bulunmadığını gösterir.")


print("Replace metodu; Bu metod ile karakter dizisinde arama yapıp, "
      "bulunan değerleri başka değerlerle değiştirebiliriz.")
print(f"Replace örneği;{mesaj.replace('Ramazan','Tayfun').replace('TOLGAY','ÖZTAN')} ")
print("Bu örnekleri farklı şekilde çoğaltabiliriz.", mesaj.replace(' ', '*'))


print(f"center metodu; Bu metod bellirli bir alan oluşturup yazıyı ortalar.\n{mesaj.center(100)}")
print("\nDikkat ettiyseniz çıktının sağında ve solunda eşit miktarda boşluk oluşturup mesajımızı ortaladı.")
print(f"Daha iyi anlamanız için aağıdaki örneği inceleyiniz;\n{mesaj.center(100,'*')}")


print("Bu ders de burada biter!")

print("Daha fazla metot için;")
print("https://www.w3schools.com/python/python_ref_string.asp adresini ziyaret edin.")
