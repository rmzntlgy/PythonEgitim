"""Listede olmayan bir elemana erişim denemesi IndexError'a neden olur.
Stringler gibi bazı tipler listeler gibi indislenebilir.
İndislenmiş stringler, strinteki her karakteri içeren bir liste gibi davranır.
Tamsayı gibi diğer tipler için indisleme mümkün değildir ve bir TypeError'neden olur"""

string = "Hello world!"
print(string[8])
