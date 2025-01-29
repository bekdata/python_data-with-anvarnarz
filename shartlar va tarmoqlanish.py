# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 08:57:02 2025

@author: utoshboltayev
"""

# 10-dars | if-else haqida 
# avtolar = ['kia', 'toyotta', 'prado', 'cobalt', 'bmw']
# for avto in avtolar:
#     if avto == ['bmw', 'kia']:
#         print(f"Bizda {avto.upper()} avtomobil mavjud")
#     else:
#         print(f'Bizda {avto.title()} avtomabili mavjud')
        
#qiymatlar teng emasligini tekshirish
# ism = input("Xush kelibsiz, \nIsmingizni kiriting: ")
# if ism.lower() == 'ali':
#     print(f"Xush kelibsiz {ism.title()}")
# else:
#     print(f"Kechirasiz {ism.title()} sizni kutmayotganotgan edik. ")

# # amaliyot
# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# for car in cars:
#     if car != 'gm':
#         print(f"{car.title()}")
#     else:
#         print(f"{car.upper()}")

# login = input("Login ma`lumotlaringiz kiriting: ")
# if login == 'admin':
#     print("Xush kelibsiz admin ")
# else: 
#     print(f"Xush kelibsiz {login.lower()}")

# son = int(input("son kiriting: "))
# if son >= 0:
#     print(son**0.5)
# else:
#     print("Musbat son kiriting ")

# 11-dars | Bir necha shartlarni tekshirish
# yosh = int(input("Yoshingizni kiriting:   "))
# if yosh < 7: 
#     print ("Siz maktab o`quvchisi emassiz ")
# elif (yosh >= 7 and yosh <=18):
#     print("Siz maktab o`quvchisi ekansiz")
# else:
#     print("Siz maktab o`quvchisidan katta ekansiz")
    
# # list elementlari orqali ro`yxatni tekshirish
# taom = input("Taom nomini kiriting:   ")
# ovqat = ['osh', 'manti', 'kabob', 'gosht']
# if taom in ovqat:
#     print("Bizda bunday ovqat mavjud")
# else:
#     print("Sizga kerakli taom bizda mavjud emas ekan")

## amaliyot 
# son = int(input("Juft son kiriting: "))
# if son %2 == 0:
#     print("Juft son kiritildi")
# else: 
#     print("Bu son juft emas")

# yoshingiz = int(input("Yoshingizni kiritin:   "))
# if (yoshingiz < 4 or yoshingiz > 60):
#     print("Sizga kirish bepul ekan")
# elif (yoshingiz <18 and yoshingiz > 4):
#     print("Siz uchun kirish narxi 10000 som")