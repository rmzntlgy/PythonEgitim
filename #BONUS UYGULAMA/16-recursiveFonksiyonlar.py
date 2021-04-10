# Recursive - özyinelemeli fonksiyonlar

def faktoriyel(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * faktoriyel(n - 1)


f = faktoriyel(5)
print(f)


def dizitopla(dizi1):
    if len(dizi1) == 1:
        return dizi1[0]
    else:
        return dizi1[0] + dizitopla(dizi1[1:])


dizi = [2, 4, 5, 6, 7, 8, 1, 0, 1]
toplam = dizitopla(dizi)
print(toplam)
