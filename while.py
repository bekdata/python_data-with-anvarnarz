# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 21:37:41 2025

@author: utoshboltayev
"""

## 17-dars | while tsikli

# #input() funksiyasini qo`llash
# ism = input("Ismingizni kiriting: ")
# savol = f"Salom {ism.title()}. Yoshingiz nechida: "
# yosh = input(savol)
# height = input(f"{ism.title()}, iltimos, bo`yingiz balandligini ham kiriting ")

## while sikli bilan tanishish
# son = 1
# while son <= 5:
#     print(son, end=" ")
#     son = son + 1

# # while va input() dan foydalanish
# print("Siz sonni kiriting biz kvadratini hisoblab beramiz")
# savol = "Sonni kiriting, chiqib ketish uchun 'exit' deb yozing "
# qiymat = ''
# while qiymat != 'exit':
#     qiymat = input(savol)
#     if qiymat != 'exit':
#         print(float(qiymat)**2) 

##amaliyot
# print("Keling siz yaxshi ko`radigan kitoblar ro`yxatini tuzamiz ")
# savol = "Yaxshi ko`radigan kitobingizni kiriting (ishni yakunlash uchun 'stop' so`zini kiriting): "

# while True:
#     qabul = input(savol)
#     if qabul == 'stop':
#         break
# print("yaxshi")


## 18-dars | while, ro`yxat va lug`atlar

# ismlar = []

# print("Yaqin dostlaringiz ro`yxatini tuzamiz")
# n=1
# while True:
#     savol = (f"{n} -do`stingizni kiriting ")
#     ism = input(savol)
#     ismlar.append(ism)
#     javob = input("Yana ism kiritishni xoxlaysizmi ?(ha/yoq) ")
#     if javob == 'ha':
#        n += 1
#        continue
#     else:
#         break
# print(ismlar)

# while bilan lug`atlarda
dostlar = {}
ishora = True

while ishora:
    ism = input("Do'stingiz ismini kiriting: ")
    yosh = input(f"{ism.title()}ning yoshini kiriting: ")
    dostlar[ism] = int(yosh) # ism kalit, yosh qiymat
    
    javob = input("Yana ma'lumot qo'shasizmi? (ha/yo'q)")
    if javob == "yo'q":
        ishora = False

for ism, yosh in dostlar.items():
    print(f"{ism.title()} {yosh} yoshda")































