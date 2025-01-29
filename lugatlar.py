# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 12:16:24 2025

@author: utoshboltayev
"""

## 14-dars | lug`atlar bilan tanishuv
# car_0 ={'model':'ferrari', 'rang':'qora'}
# print(car_0['model']) #bitta qiymatiga murojaat qilish
# print(car_0)   # lug`at elementini chaqirish
#talaba haqida lug`at yaratamiz 
# talaba_0 = {"ism":"Abror", 'familya':'Qulsoatov', 'yosh':24, 't_yil':2000}
# print(talaba_0)   #lug`at tarkibini ko`rsatish

# #lug`at elementlaridan foydalanib ma`lumot tayyorlash
# print(f'Talabaning ismi - {talaba_0['ism']} \n tugulgan yili {talaba_0['t_yil']}- yilda tugulgan')  

# #lugatga yangi qiymatlar qo`shish
# talaba_0['kurs'] = 5
# talaba_0['fakultet'] = 'informatika'
# print(talaba_0)

# #bo`sh lug`atga element qo`shish
# student = {}
# student['ism'] = 'bo\`riyev hakimjon'
# student['yosh'] = 25
# student['university'] = 'TerDU'
# print(student)

# #foydalanuvchi va telefoni haqida ma`lumotlar
# telefonlar = {
#     'ali':'redmi',
#     'vali':'honor',
#     'husan':'iphone',
#     'hasan':'techno X'
#     }
# phone = telefonlar['ali']
# print(f"Alining telefoni {phone}")

# #lug`atlarda get() metodidan foydalanish
# tel = telefonlar.get('Sobir', 'Bunday ism mavjut emas')
# print(f"Sobirning telefoni - telefoni {tel} ")

##amaliyot
# akam = {}
# akam['ism'] = "Hasanov sobir"
# akam['manzil'] = ["Surxondaryo"]
# akam['t_yil'] = 1996
# print(f"Mening akam {akam['ism'].title()}, {akam['t_yil']}-yilda {akam['manzil']} viloyatida tavallud topgan ")

## 15-dars | Lug`at elementlari bilan ishlash
# talaba_0 = {
#     'ism':'Alijon',
#     'familya':'Valijonov',
#     'manzil':'Surxondaryo',
#     't_yil':2000
#     }
# print(talaba_0.items())  #lug`at elementlari haqifda 

# for kalit, qiymat in talaba_0.items():
#     print(f"kalit: {kalit}")
#     print(f'qiymat: {qiymat}')

davlatlar = {
    "o'zbekiston":{'poytaxt':"toshkent",
                   'maydon':448978,
                   'aholi':33_000_000,
                   'pul birligi':"so'm"
                   },
    "rossiya":{'poytaxt':"moskva",
                   'maydon':17_098_246,
                   'aholi':144_000_000,
                   'pul birligi':"rubl"
                   },
    "aqsh":{'poytaxt':"vashington",
                   'maydon':9_631_418,
                   'aholi':327_000_000,
                   'pul birligi':"dollar"},
    "malayziya":{'poytaxt':"kuala-lumpur",
                   'maydon':329750,
                   'aholi':25_000_000,
                   'pul birligi':"rinngit"}
    }

for davlat, info in davlatlar.items():
    if davlat.lower() == 'aqsh':
        davlat = davlat.upper()
    else:
        davlat = davlat.capitalize()
        print(f"\n {davlat}nig poytaxti {info['poytaxt'].title()}")








