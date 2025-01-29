## 19-dars | Funksiyalar
# def salom_ber():
#     """Foydalanuvchi bilan salomlashadigan funksiya"""
#     print("Assalomu alaykom")

# salom_ber()

#foydalanuvchilarnig har biriha 
# def salomlash(ism):
#     """ismi orqali salom beradigan funksiya"""
#     print(f'Assalomu alaykom {ism.title()}')

# mehmonlar = ['hasan', 'olim', 'sobir', 'murod']
# for mehmon in mehmonlar:
#     salomlash(mehmon)

# def data_person(ism, familya):
#     """Ism va familyasini aytuvchi funksiya """
#     print(f"foydalanuvchining ismi - {ism.title()} \nfodalanuvchinin familyasi - {familya.title()}")
    
# data_person("ulug`bek", "Toshboltayev")

# # amaliyot
# def person (ism, yosh):
#     """yosh va ism so`rab tug`ulgan yilni qaytaruvchi kod"""
#     print(f"{ism.title()} siz {2025-yosh} -yilda tug`ulan ekansiz")

# ism = input("Ismingizni kiriting: ")
# yosh = int(input(f"{ism} yoshingizni ham kiriting: "))
# person(ism, yosh)

   
## kiritiulgan son kvadrat va kubini hisoblash    
# def hisobla (son):
#     """Kvadrat va kubni qaytaruvchi dastur yozish"""       
#     print(f"{son} nig kvadtari {son**2} ga teng")
#     print(f"{son} ning kubi {son**3} ga teng ")

# son = int(input("Sonni kiriting: "))
# hisobla(son)

## kvadrat va kubni hisoblashni while bilan birga qo`llash
# ishora = True
# while ishora:
#     savol= input("Hisoblashni bajarishni xoxlaysizmi (ha/yoq)")
#     if savol.lower() == 'ha':
#         def hisobla (son):
#             """Kvadrat va kubni qaytaruvchi dastur yozish"""       
#             print(f"{son} nig kvadtari {son**2} ga teng")
#             print(f"{son} ning kubi {son**3} ga teng ")

#         son = int(input("Sonni kiriting: "))
#         hisobla(son)
#     else:
#         ishora = False


## ikkita son berilgan shu sonlardan kattasini qaytaruvchi
# def taqqosla(a, b):
#     if (a>b):
#         print(f'katta son {a} ekan')
#     elif (a<b):
#         print(f'katta son {b} ekan')
#     else:
#         print("ikkala son teng ekan")

# a = int(input("a soniga qiymat kiriting: "))
# b = int(input("b soniga qiymat kiriting: "))
# taqqosla(a, b)



## 20-dars | Qiymat qaytaruvchi funksiya

# funksiyadan qaytgan qiymatni olish
# def person(ism, familya):
#     """funksiyadan qaytgan qiymatni o`zgaruvchiga saqlash"""
#     toliq_ism = (f"ism familyangiz - {ism.title()} {familya.title()}")
#     return toliq_ism

# talaba = person('men', 'sen')
# print(talaba)

# def oraliq (min, max):
#     sonlar = []
#     while min < max:
#         sonlar.append(min)
#         min += 1
#     return sonlar

# sonlar = oraliq(10, 100)
# print(sonlar)


## ro`yxat va lug`atlar bilan birga massiv yaratish
# def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
#     avto = {'kompaniya':kompaniya,
#             'model':model,
#             'rang':rangi,
#             # 'korobka':korobka,
#             'yil':yili}
#             # 'narh':narhi}
#     return avto

# print("Avtomobillar ro`yxatini tuzamiz")
# avtolar = []
# while True: 
#     print("Avtomobillar haqidagi ma`lumotlarni kiriting: ")
#     kompaniya = input("kompaniyasi haqida ma`lumotlarni kiriting: ")
#     model = input("Model ma`lumotini qo`shing: ")
#     rangi = input("Avtomobil rangini kiriting: ")
#     t_yili = int(input("Ishlab chiqarilgan yili: "))
    
#     avtolar.append(avto_info(kompaniya, model, rangi, t_yil))
    
#     javob = input("yana avto qo`shasizmi (ha/yoq) ")
    
#     if javob == 'no':
         # break



## 21-dars | fumksiya va ro`yxat 
# funksiyaga ro`yxat uzatish
# def baxola(ismlar):
#     baxolar = {}
#     while ismlar:
#         ism = ismlar.pop()
#         baxo = input(f'{ism.title()}nig baxosini kiriting: ')
#         baxolar['ism'] = baxo
#         return baxolar
    
# talabalar = ['ali', 'vali', 'hasan', 'hasan']
# baxolar = baxola(talabalar)
# print(baxolar)

## amaliyot
# def katta_harf(ismlar):
#     katta_ism = []
#     for ism in ismlar:
#         katta_ism.append(ism.title())
#     return katta_ism

# talaba = ['ali', 'vali', 'hasan', 'husan']
# katta_ism = katta_harf(talaba)
# print(katta_ism)

# print(talaba  # mana o`zgarmagan)



## 22-dars | Moslashuvchan funksiya (*args, **kwargs)

# def summma(*sonlar):
#     """Kiritilayotgan sonlar yig`indisini hisoblash"""
#     hisob = 0
#     for son in sonlar:
#         hisob += son
#     return hisob

# print(summa(1,2,3))
# print(summa(1,2,3,4,5,6,7,8,9))

#  majburiy qiymatlarni kiritish talab qilinganda 
# def summa(a, b, *sonlar):
#     yigindi = 0
#     for son in sonlar:
#         yigindi += son
#     return yigindi
# print(summa(1,2,3))
# print(summa(1))   # bu xolatda kod xatolik beradi


## kwargs usulidan foydalanish
# def avto_info(kompaniya, model, **malumotlar):
#     """avtomobillar haqidagi ma`lumotlarni yig`ish"""
#     malumotlar['kompaniya'] = kompaniya
#     malumotlar['model'] = model
#     return malumotlar

# avto1 = avto_info("gm", "malibu", rang='qora', yil=2012)
# print(avto1)


## amaliyot
# def summa(*sonlar):
#     """Yig`indini hisoblash"""
#     natija = 0
#     for son in sonlar:
#         natija += son
#     return natija
 
# print(summa(10,20,30,40,50,60,70,80,90))


def talaba (ism, familya, **malumotlar):
    """Talaba haqidagi malumotlar"""
    malumotlar['ism'] = ism
    malumotlar['familya'] = familya
    return malumotlar

print(talaba('hakim', 'zokirov', kurs = '5-kurs', manzil= 'Surxondaryo'))



## 23-dars | Modullar

