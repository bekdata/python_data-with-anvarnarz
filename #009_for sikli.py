# -*- coding: utf-8 -*-
"""
Created on Sun Aug  3 21:09:53 2025

@author: user
"""
"""For sikli bilan tanishish"""

# ro`yxat ko`rinishida tasvislash uchun
# sonlar = list(range(1, 10))
# print(sonlar)

# for bilan sonlar ketma-ketligini hosil qilish
# sonlar = list(range(1,100))
# for son in sonlar:
#     print(son)
    
# ismlar = ['ali', 'vali', 'hasan', 'husan']
# for ism in ismlar:
#     # print("Assalomu alaykom",  ism.title())   # birinchi usul
    # print(f"Assalomu alaykom {ism.title()}")  # ikkinchi usul


#foydalanuvchidan ma`lumot so`rab for sikli ishlatish
# ismlar = []
# for son in range(3):
#     ismlar.append(input(f'{son+1}-ism kiriting: '))
# print(ismlar)


#if va for operatorlari birga  
ismlar = []
for n in range(3):
    ism = input(f"{n+1} - do`stingizni ismini kiriting: ")
    if len(ism) >= 3:
        ismlar.append(ism.title())
    else:
        print("Bunday ism mavjud emas")
print(ismlar)