print("Merhaba bu ilk paython çıktısıdır")  #python ekrana basma komutu bu şekildedir. Basit ve eğlenceli

print(2+2) #aritmatik işlemleri bu şekilde kolaylıkla yapabilirsiniz ekrana direkt olarak toplamı verecektir.


#buradan sonraki işlemlerde değer atama yapıyoruz.

ramazangelir = 5000 #ramazangelir diye değer atadık bu değeri daha sonraki işlemlerimizde kullanacağız.

yil = 12 #bir yıl 12 aydan oluşur bu yüzden yil değişkenimizde 12 değerini atadık.

print(ramazangelir*yil)  #evet yıllık maaşımızı bu şekilde hesaplayabiliriz.

#değişken tanımlama kuralları
#birinci kural:     değişkenler rakam ile başlayamaz!

sayi=1          #sayi değişkenine 1 değerini atadık
print("ilk atanan değer=",sayi)     #sayi değişkenini ekrana çıktı olarak aldık
sayi=2          #sayi değişkenine daha sonra tekrar değer atadık ve atadığımız son değer artık önceki değerin yerine geçti
print("son atanan sayı değeri=",sayi)     #son değerini bu çıktı ile görüyoruz.

sayi += 5 #buradaki işlem sayi değişkeni değerini 5 sayı arttırmadır.
print("ekleme yapıldıktan sonraki değer=",sayi)

#ikinci kural:      büyük-küçük harf duyarlı bir programlama dilidir python

dogumyili = 1995

print(dogumyili)

#print(DogumYili) bu tarz ifade ile çağırırsanız hata verecektir. Değişken oluştururken dikkat edin!


#Değişken ve diğer atama işlemlerinde Türkçe karakter kullanmayın.
#hata vermeyecektir fakat pek tavsiye edilmez

doğumyılı = 1995
print("Türkçe karakter atama yapıldığındaki sonuç=",doğumyılı)



dogumgunu = 3 #bu ifade interger türü bir veridir.

dogumayi = "3" #bu ise bir string türü ifadedir.

dogumgunu,dogumayi,dogumyili = 3,3,1995 #burada tek satırda atama işlemlerini yapmış olduk.

y = 5
x = 3.1
k = True

print("Y değişken tipi",type(y))
print("x değişken tipi",type(x))
print("k değişken tipi",type(k))

print("İnt to Float =",float(y))    #burada integer türündeki ifadeyi float türüne değiştirme yapıldı.
print("float to int =",int(y))      #burada float türündeki ifadeyi integer türüne değiştirme yapıldı.
print("bool to int=", int(k))       #burada bool türündeki ifadeyi integer türüne değiştirme yapıldı.
print("bool to float=", float(k))   #burada bool türündeki ifadeyi float türüne değiştirme yapıldı.




