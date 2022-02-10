
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
# netice = (i for i in range(1,10))
# print(next(netice))
# print(next(netice))
# print(next(netice))
# print(next(netice))
# print(next(netice))


#!Nested function Pythonda yeni encapsulation deyilir buna nested functionlata yeni
# def function1():
#     print('Hello OUTER function')
#     def function2():
#         print('hello INNER function')
#     function2()
# function1()

# def col_funksiya(sayi1):
#     print('Col funkciyasi isleyir',sayi1)
#     def iceri_funksiya(sayi2):
#         print('Iceri funksiya isleyir',sayi2)
#     iceri_funksiya(10)
# col_funksiya(15)

# def faktorial(sayifaktoreial):
#     def icfaktorial(sayi):
#         if(sayi<=1):
#             return 1
#         return sayi * icfaktorial(sayi-1)
#     return icfaktorial(sayifaktoreial)#5
    
# print(faktorial(5))

# def faktorial(number):
#     if not isinstance(number,int):
#         raise TypeError('Girdiginiz veri tamsayi olmlaididir')
#     if not number>=0:#yeni eger gonderilen deyer 0 dan boyuk deyilse not number>=0 yeni
#         raise ValueError('Girdihiniz sayi sifirdan buyuk olmalidir')#js de xeta atmag ucun throw dan istifade olunur
#     def icerifaktorial(disfuncgelendeyer):
#         if disfuncgelendeyer <=1:
#             return 1
#         return disfuncgelendeyer * icerifaktorial(disfuncgelendeyer-1)
#     return icerifaktorial(number)

# try:
#     print(faktorial(-5))
# except Exception as e:
#     print('Gelen xeta {}'.format(e))

#!Ic ice funksiya donderme closures yeni baglama,kapanma
# def kokFunksiya(reqem):
#     def balaFunksiya(ust):
#         return reqem**ust
#     return balaFunksiya


# x = kokFunksiya(5)
# print(x(2))

# def adiniSoyle(isim):#clouseres funksiyalari isletmek ucun icerideki yeni nested funksiyani geri dondermek lazimdir
#     def adinDogru(ad):
#         if isim == ad:
#             return 'Isminiz Dogru'
#         else:
#             return 'Isminiz hatali'
#     return adinDogru

# x = adiniSoyle('riad')
# print(x('tural'))

def islem(islem_adi):
    
    def topla(*args):
        cem = 0
        for i in args:
            cem+=i
        return cem

    def vurma(*args):
        hasil = 1
        for j in args:
            hasil*=j
        return hasil
    
    if islem_adi == 'toplama':
        return topla
    elif islem_adi == 'vurma':
        return vurma
    else:
        raise ValueError('Hata Olustu')
    
#eger funksiyani parametre hissesine *args ve **kwargs vermisense for seklinde rahat yaza bilersen cunki => *args bir tupledir, **kwargs ise bir dictionarydir yeni key ve value seklinde istifade olunur
netice = islem('toplama')
print(netice(1,2,3,4,5))

netice2 = islem('vurma')
print(netice2(1,2,3,4,5))
