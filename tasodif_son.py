# -*- coding: utf-8 -*-
"""
Created on Sun Aug 10 21:31:09 2025

@author: user
"""

"""Tasodifiy sonni aniqlash uchun kod """

import random

# Chegarani so'rash
data = int(input("Chegara uchun qiymat sonini kiriting: "))

# Tasodifiy sonni oldindan o'ylab olish
son = random.randint(1, data)

def son_top():
    """Foydalanuvchidan son so`rash"""
    while True:
        print(f"Men 1 dan {data} gacha bo`lgan son o`yladim. Topa olasizmi?")
        qiymat = int(input("Topish uchun sonni kiriting: "))
        
        if qiymat == son:
            print("Siz to`g`ri javob berdingiz 🎉")
            break
        elif qiymat < son:
            print("Men o‘ylagan son kattaroq.")
        else:
            print("Men o‘ylagan son kichikroq.")

son_top()

    
    





















