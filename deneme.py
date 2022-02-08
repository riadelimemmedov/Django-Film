
#!Generatorlar Classlarda Python => yeni ramda datanin istidesine qenaet etmek ucun istifa olunan bir yoldur Generatorlar

# def sayac(maxvalue):
#     sayi = 1
#     sayilar = []
#     while sayi<=maxvalue:
#         sayilar.append(sayi)
#         sayi+=1
#     return sayilar

# print(sayac(20))

#*Indi ise Generator ile yazag bu kodlari
# def sayac(maxvalue):
#     startvalue = 1
#     while startvalue<=maxvalue:
#         yield startvalue
#         startvalue+=1
#generatorlar ozleri bir decoratordur ele
# netice = sayac(20)
# print(next(netice))
# print(next(netice))
# print(next(netice))
# print(next(netice))
# print(next(netice))
# for i in sayac(20):
#     print(i)

#*List Comprehension istifadesi
# netice = [i for i in range(20)] => Bu cur yazilis GENERATOR ola bilmez
#?eger list comprehension ile decorator yazmag isteyirnsense list yox tuple yeni demetlerden istifade ele =? () yeni bu es6 syxtax sal yadiva => yadda saxla tuple
#?eger generatordaki deyeri ekrana yazdirmag isteyirsense => next() den istifade et iteratorlardaki kimi
netice = (i for i in range(1,10))
print(next(netice))
print(next(netice))
print(next(netice))
print(next(netice))
print(next(netice))


