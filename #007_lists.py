# -*- coding: utf-8 -*-
"""
Created on Fri Aug  1 17:04:22 2025

@author: user
"""

"""Pythonda List(Ro`yxatlar)"""
# data = [10,20,30,40]
# print(data[0]) #bitta elementni chaqirish
# print(data[3])
# print (data)


# meva = ['olma', 'anor', 'banan', 'nok']
# print(meva)

# sonlar = ['bir', 'ikki', 3,4,5,6,8,9]
# print(sonlar[-1]) #oxirgi elementni chiqarish
# print(sonlar)


# meva = ['olma', 'anor', 'banan', 'nok']
# print(meva[0].upper()) # hamma harfni katta qilib yozish
# print(meva[1].lower()) # hamma harfni kichik qilish
# print(meva[2].title()) # bosh harf bilan yozishga amal qiladi
# print(meva)

#Jadval elementlarini almashtirish
# meva[0] = 'shaftoli'
# print(meva)

#append() - ro`yxat oxiriga element qo`sh
# meva.append('o`rik')
# print(meva)

#insert()
# meva.insert(0, 'fruit') #ko`rsatilgan index bo`yicha qiymat qo`sh
# print(meva)


# new_list = []
# print(new_list)

# new_list.append("kivi")
# new_list.append("ananas")
# new_list.insert(0, "tarvuz")
# new_list.insert(3, "qovun")
# print(new_list)

# del new_list[0]   #index orqali elementni o`chirish
# new_list.       #o`chirishni ikkinchi turi edi

# print(new_list)

data = [1,2,3,4,5,6,7,8,9]
bek = []

print(data)
print(bek)

bek = data.pop(0)

print("data:", data)
print("bek:", bek)
