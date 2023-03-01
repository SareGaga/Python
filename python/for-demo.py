sayılar = [1,3,5,7,9,12,13,14]

#1- sayılar listesindeki hangi sayılar 3 ün katı ?

# for sayi in sayılar:
#     if(sayi%3==0):
#         print(sayi)

#2- sayılar listesindeki sayıların toplamı

# toplam=0
# for sayi in sayılar :
#     toplam += sayi
# print("toplam :", toplam)

#3- sayılar listesindeki tek sayıların karesi

# for sayi in sayılar :
#     if(sayi % 2 == 1):
#         print(sayi **2)

sehirler = ["kocaeli","istanbul","ankara","izmir","rize"]

#4- sehirlerden hangileri en fazla 5 karakterli

# for sehir in sehirler :
#    if (len(sehir) <= 5):
#     print(sehir)

urunler =[
    {"name":"samsung s6","price" :"5000"},
    {"name":"iphone 11","price" :"16000"},
    {"name":"iphone 13","price" :"20000"},
    {"name":"iphone 14","price" :"30000"}
    

]

#5- urunlerin fiyat toplamı

# toplam =  0
# for urun in urunler:
#     fiyat = int(urun["price"])
#     toplam += fiyat
# print(toplam)

#6- ürünlerden fiyatı en fazla 9000 olan ürünler

# for urun in urunler:
#    if (int(urun["price"]) < 9000):
#     print(urun["name"])