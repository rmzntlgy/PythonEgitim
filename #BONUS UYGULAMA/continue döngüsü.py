i = 0
while True:
    i += 1
    if i == 2:
        print("atlanıyor")
        continue
    if i == 5:
        print("çıkılıyor")
        break
    print(i)
print("bitti")


"""python dili satır girintilerine dikkat edilmesi gerekli print("bitti) komutu, print(i) ile aynı girintide olursa
program istediğimiz şekilde çalışmaz"""
