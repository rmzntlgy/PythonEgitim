print("Yarı çapı verilen alanın çevresini ve alanını hesaplama programı.(pi=3.14")

pi  = 3.14

r   = float(input("yaricap="))

cevre = 2*pi*r
alan = pi*(r**2)
print("Alan:",alan,"\nÇevre:",cevre)

#birleştirme işlemi yaparken veri türlerine dikkat et. İnteger ile bir string ifadeyi toplayamazsın.
#veri tipi dönüştürme işlemleri ile bu hatalardan kaçın.
