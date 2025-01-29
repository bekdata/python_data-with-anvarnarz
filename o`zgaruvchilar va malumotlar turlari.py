# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 13:51:08 2025

@author: utoshboltayev
"""

##06dars -Sonlar bilan ishlash
# kv_tomon = 20
# kv_yuza = kv_tomon ** 2
# print(kv_yuza)


# import math
# PI = math.pi
# r = 13.5
# d_yuza = PI*r**2
# print("doira yuzi: ", d_yuza, "shu qiymatga teng ")

# #bir nechta sonlarni chiqarish
# x, y, z = 10, 11, 12 
# print(x,y,z)

# #foydalanuvchidan ma`lumot so`rash
# son = input("foydalanish uchun sonni kiriting, (bu yerga : ")
# matn = input("foydalanish uchun matn kiriting: ")

# print(son)
# print(matn)

##amaliyot
# qiymat = int(input("hisoblash uchun sonni kiriting:  "))
# print(f"{qiymat} ning kvadrati {qiymat **2} ga teng")
# print(f"{qiymat} ning kubi {qiymat **3} ga teng")

# yosh  = int(input("tug`ilgan yilingizni kiriting: "))
# print(f"Siz {2025-yosh} yoshda ekansiz")

# son1 = int(input("birinchi sonni kiriting: "))
# son2 = int(input("ikkinchi sonni kiriting: "))

# print(son1 + son2)
# print(son1 - son2)
# print(son1 * son2)
# print(son1 / son2)



#07-dars | list (ro`yxat)
# sonlar = [10,20,30,40,50,60,70,80,70,80,90]
# sonlar.append(100) # qator oxirisida element qo`shish
# sonlar.insert(0, '0')  # elementni tartib raqamiga qarab joylashtirish
# del sonlar[0]  # 0 tartib raqamdagi elementni o`chirishda
# sonlar.remove(50)  # 50 elementni aniqlash
# print(sonlar)

# # amaliyot
# ismlar = ['ali', 'vali', 'hasan']
# print(ismlar)
# print(f"{ismlar[0].title()} bugun choyxona bormi")
# print(f"ha {ismlar[1].title()}, bugun choyxona Hasanlarni uyida bo`ladi ")

# sonlar.append(12)
# sonlar.insert(12, 12365)
# del sonlar[12]
# sonlar.remove(12)
# print(sonlar)


# # 08-dars | Ro`yxatlar bilan ishlash
# cars = ['tiko', 'damas', 'nexia', 'cobalt', 'malibu']
# print(cars)
# cars.sort()   # ro`yxatni tartiblash
# print(cars)
# print(len(sonlar))   # elementlar son ini aniqlash

# print(list(range(10,20))) # shu oraliqdagi sonlarni chiqarish


# son = list(range(1,50,4))
# print(min(son)) # kichik sonni topish.
# print(max(son))


# print(son[5:])
# print(son[:9])

# harf = ['a','k','b','l','d','s','u']
# harf.sort()
# print(harf)

#amaliyot
# country = ['uzb', 'rus', 'kor', 'kaz', 'avs']
# print(len(country))   # ro`yxat uzunligi
# print(sorted(country))     #davlat nomlarini tartib bilan chiqarish

# sorted(country, reverse=True)  #teskari tartib bilan ro`yxatni chiqarish

# son = list(range(120, 1202,2))
# print(max(son))#kattasini qaytarish
# print(min(son)) #kichik sonni qaytarish
# print(f"sonlar o`rtasidagi ayirma:  {max(son) - min(son)} ga teng ekan ")

# taom = ['osh', 'manti', 'kabob', "choy"]
# taom_copy = taom[:]
# print(taom)

# taom_copy.append('shorva')
# taom_copy.append('baliq')
# print(taom_copy)

# nonushta = tuple(taom_copy)     # tuple(o`zgarmas ro`yxatga aylantirish)
# print(type(nonushta))     # ro`yxat turini ko`rish
# print(nonushta)   # tupleni chiqarish


# #09-dars | for takrorlash operatori
# #matnli ro`yxatlar bilan 
# abonentlar = ['Ali', 'Vali', 'Hasan', 'Husan', 'Botir']
# for abonent in abonentlar:
#     print(f" Assalomu alaykom {mexmon}, Sizni oylik xisobingiz o`chirildi. Xizmatni faollashtirish uchun iltimos xisobingizni to`ldiring ")
    
# #sonli ro`yxatlar bilan
# sonlar = list(range(20))
# for son in sonlar:
#     print(f"{son}ning kvadrati {son**2} ga teng")

# dostlar = []
# print(f"5 ta eng yaqin do`stingizni kiriting:")
# for n in range(5):
#     dostlar.append(input(f"{n+1} - do`stingizni ismini kiriting: ").title())
# print(dostlar)

##amaliyot
# ismlar = ['ali', 'vali', 'hasan', 'husan', 'toyir']
# for ism in ismlar:
#     print(f"Assalomu alaykom  {ism.title()} ")
# print("Mexmonimiz bo`lganingizdan hursandmiz")

sonlar = list(range(11,100,2))
for son in sonlar:
    print(f"{son} ning kubi {son**3} ga teng")