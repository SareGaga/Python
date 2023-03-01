# 1- kullanıcıdan isim ,yaş ve eğitim bilgilerini isteyip ehliyet alabilme durumu kontrol

# isim= input("isminiz :")
# yas=int(input("yaşınız"))
# egitim=input("eğitim :")

# if (yas>=18):
#      if (egitim=="lise" or egitim=="üniversite") :
#       print(f"b{isim} ehliyet alabilirsiniz")
#      else:
#         print(f"{isim} ehliyet alamazsın eğitim durumunuz yetersiz.")

# else:
#     print(f"{isim} ehliyet alamazsın yaşın tutumuyor.")




#2- Bir öğrencinin 2 yazılı bir sözlü notunu alıp hesaplanan ortalamaya göre not aralığına karşılık gelen not bilgisini yazdır


# vize1= int(input("vize1 :"))
# vize2=int(input("vize2"))
# sözlü=int(input("sözlü"))


# ortalama = (vize1+vize2+sözlü)/3

# if (ortalama >=0) and (ortalama< 25):
#     print(f"ortalamanız : {ortalama} notunuz: 0 ")
# elif (ortalama>=25) and(ortalama<45):
#         print(f"ortalamanız : {ortalama} notunuz: 1")
# elif (ortalama>=45) and(ortalama<55):
#         print(f"ortalamanız : {ortalama} notunuz: 2")
# elif (ortalama>=55) and(ortalama<69):
#         print(f"ortalamanız : {ortalama} notunuz: 3")
# else :
#     print("yanlış bilgi girdiniz. ")





#3- tarfiğe çıkış tarhi alınan bir aracın servis zamanını aşağıdaki bilgilere göre hesaplayınız.

import datetime

tarih =input("aracınız hangi tarihte trafiğe çıktı  (2019/8/9) : ")
tarih = tarih.split('/') # girilen tarihi / ile ayrımamızı sağlıyor split 
tarfigeCıkıs= datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))
simdi = datetime.datetime.now() # şimdiki tarih bilgisini vericek
fark= simdi-tarfigeCıkıs
days=fark.days # farkı güne çevirdik

if days <=365:
    print("1. servis aralığı")
elif days > 365 and days <=365*2:
    print("2.servis aralığı")
elif days > 365*2 and days<=365*3:
    print("3.servis aralığı")

else:
    print("hatalı süre")
