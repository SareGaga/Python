
# 1-100 arasında rastgele sayıyı buldurmaya çalışın

import random

sayı = random.randint(1,10)
can = int (input("kaç hak kullanmak istersiniz"))
hak = can
sayac = 0

while hak > 0 :
    hak -= 1
    sayac += 1
    tahmin = int(input("tahmin:"))

    if sayı == tahmin :
        print(f"tebrikler {sayac}. defada bildiniz. Toplam puanınız : {100 - (100/can) * (sayac-1)}")
        break
    elif sayı > tahmin:
        print("yukarı")
    else:
        print("aşağı")

    if hak == 0:
        print(f"hakkınız bitti. Tutulan sayı : {sayı} .")
