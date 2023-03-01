# 1- Gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazın.

def yazdır(kelime,adet):
    print(kelime * adet)
yazdır("merhaba\n", 10)



# 2- Kendine gönderilen sınırsız sayıdaki parametreyi bir listeye çeviren fonk


def listeyeCevir(*params):
    liste = []
    for param in params:
        liste.append(param)
    return liste

result= listeyeCevir(110,20,30,"merhaba")
print(result)




# 3- Gönderilen 2 sayı arasındaki tüm asal sayıları bulun


def asalSayılarıBul(sayi1,sayi2):
    for sayi in range(sayi1,sayi2+1):
        if sayi > 1 :
            for i in range(2,sayi):
                if (sayi % i == 0 ):
                    break
                else:
                    print(sayi)

sayi1 = int(input("sayı 1 :"))
sayi2 = int(input("sayı 2 : "))

asalSayılarıBul(sayi1, sayi2)






# 4- Kendisine gönderilen bir sayının tam bölenlerini bir liste şek döndür.


def tamBolenleriBul(sayi):
    tamBolenler = []

    for i in range(2,sayi):
        if (sayi % i == 0):
            tamBolenler.append(i)

    return tamBolenler

print(tamBolenleriBul(20))