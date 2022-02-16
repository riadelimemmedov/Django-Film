
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

# def islem(islem_adi):
    
#     def topla(*args):
#         cem = 0
#         for i in args:
#             cem+=i
#         return cem

#     def vurma(*args):
#         hasil = 1
#         for j in args:
#             hasil*=j
#         return hasil
    
#     if islem_adi == 'toplama':
#         return topla
#     elif islem_adi == 'vurma':
#         return vurma
#     else:
#         raise ValueError('Hata Olustu')
    
# #eger funksiyani parametre hissesine *args ve **kwargs vermisense for seklinde rahat yaza bilersen cunki => *args bir tupledir, **kwargs ise bir dictionarydir yeni key ve value seklinde istifade olunur
# netice = islem('toplama')
# print(netice(1,2,3,4,5))

# netice2 = islem('vurma')
# print(netice2(1,2,3,4,5))

#!Pythondaki en sonuncu indexi alma deyerin

# # Python 3 code to demonstrate 
# # accessing last element of list
# # using naive method 
  
# # initializing list 
# test_list = [1, 4, 5, 6, 3, 5]
  
# # printing original list 
# print ("The original list is : " + str(test_list))
  
# # First naive method
# # using loop method to print last element 
# for i in range(0, len(test_list)):
  
#     if i == (len(test_list)-1):
#         print ("The last element of list using loop : "
#                                   +  str(test_list[i]))

# # Second naive method        
# # using reverse method to print last element
# test_list.reverse()
# print("The last element of list using reverse : "
#                             +  str(test_list[0]))


#!Pythondaki decaoratolar

#Burdaki numune decorator deyil decoratorun evezedicisidir
# def salamla(fn):
#     def innner():
#         print('Salamla isledi')
#         fn()
#     return innner


# def gunaydin():
#     print("Merhaba riad")

# a = salamla(gunaydin)
# a()


#!Indi ise decoratordan istifade edek

# def selamver(fn):
#     def inner():
#         print('Salam Riad')
#         fn()
#     return inner

# @selamver
# def gunaydin():
#     print('Gunaydin Riad')

# gunaydin()


#!Ornek Decorator
#?Decaratorsuz
# def make_pretty(func):
#     def inner():
#         print('l got decarated')
#         func()
#     return inner

# def ordinary():
#     print('l am ordinary')
    
# a = make_pretty(ordinary)
# a()

#?Decorator ile
# def make_pretty(func):
#     def inner():
#         print('l got decorated')
#         func()
#     return inner

# @make_pretty
# def ordinary():
#     print('l am ordinary')
    
# ordinary()

#?Decorator funksiyalara parametr gondermek
# def smart_divide(func):
#     def inner(adeyeri,bdeyeri):
#         print('Isledi decorator')
#         if bdeyeri == 0:
#             print('cannot divide')
#         else:
#             func(adeyeri,bdeyeri)
#     return inner#return innner mutleq sekilde return olmalidir

# @smart_divide
# def divide(a,b):
#     print(a/b)

# divide(10,5)

#?Ornek yene decorator
# def selamlama(func):
#     def inner(adiniz):
#         print('Fonksiyon Calisti')
#         func(adiniz)
#         print('Bitti Fonksiyonun Calismasi')
#     return inner #bura mutleq sekilde yazilmalidir yeni return innner hissesi hemcinin inner funksiyasi mutleq yazilmalidir

# @selamlama
# def gunaydin(isim):
#     print('Gunyadin',isim)
    
# @selamlama
# def iyigunler(isim):
#     print('Iyi gunler',isim)

# @selamlama
# def iyiaksamlar(isim):
#     print('Iyi aksamlar',isim)
    
# gunaydin('Riad')
# iyigunler('Tural')
# iyiaksamlar('Kenan')

#!Pythonda decoratorun eyni vaxtda hem parametreli hem parametresiz funksiyalarda istifadesidesi
#*Decorator Funksiyalarin Parametreleri
# def decoratorFunksiya(func):
#     def inner(*args,**kwargs):
#         func(*args,**kwargs)
#     return inner


# @decoratorFunksiya
# def salamVer():
#     print('Salam Sabahiniz Xeyir')
    
# @decoratorFunksiya
# def salamAdim(ad):
#     print(f"Menim adim : {ad} dir")

# salamVer()
# salamAdim('Riad')

#!Parametre alan Decoratorlar decorator funksiyalarda
# def dec_func_parametres(count):
#     def dec_funk(func):
#         def inner(*args,**kwargs):
#             for _ in range(count):# _ deyilde i ve ya ne istesen yaza bilersen
#                 func(*args,**kwargs)
#         return inner
#     return dec_funk

# @dec_func_parametres(count=2)
# def hello():
#     print('Hello')
    
# @dec_func_parametres(count=5)
# def greet(name):
#     print(f"Hello {name}")#funksiya icinde ekrana yazdiranda format metodu ile yazma cunki xeta verir
    
# hello()
# greet('Tural')

#?Numune
def decorator_root_function(func):
    def inner(rakamlarlistesi):
        cift_toplami = 0
        cift_sayilar = 0
        tek_toplam = 0
        tek_sayilar = 0
        for rakam in rakamlarlistesi:
            if(rakam%2==0):
                cift_sayilar+=1
                cift_toplami+=rakam
            else:
                tek_sayilar+=1
                tek_toplam+=rakam
        print('Cift Sayilarin Ortalamsi :', cift_toplami/cift_sayilar)
        func(rakamlarlistesi)#burani bele yazanda gedib ortalama funksiyasi isleyir => 316 setirdeki funksiya yeni
        print('Tek Sayilarin Ortalamasi :', tek_toplam/tek_sayilar)
    return inner

@decorator_root_function
def ortalama(sayilar):
    toplam = 0
    for i in sayilar:
        toplam+=i
    print('Genel Ortalama',toplam/len(sayilar))
ortalama([1,2,3,4,5,6,7,8,9,10])