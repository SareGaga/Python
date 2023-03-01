sayilar = [1,3,5,7,9,12,19,21]

# 1- sayilar listesini while ile ekrana yazdırın

# i=0 # eleman sayısını temsil ediyor.
# while(i<len(sayilar)):
#     print(sayilar[i])
#     i+=1

# 2- Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm tek sayıları ekrana yazdır


# baslangic = int(input("başlangıç :"))
# bitis = int(input("bitis :"))

# i = baslangic
# while i < bitis:
#     i += 1
#     if (i % 2 == 1 ):
#         print(i)

#3- 1-100 arasındaki sayıları azalan şekilde yaz

i = 100
while i >  0:
    print(i)
    i -= 1


#4- kullanıcıdan alacağınız 5 sayıyı ekrana sıralı yazdır

numbers =[]

i = 0 
while i < 5:
   sayi =int(input("sayi :"))
   numbers.append(sayi) # numbersın üstüne sayı ekle
   i+=1
number.sort() # sort methoduyla sıraladık.
print(numbers) 

#5- kullanıcıdan alacağınız sınırsınz ürün bilgisini ürünler listesi içinde sakla. dictionary liste yapısı name,price

urunler = []

adet =int(input("kaç ürün eklemek istiyorsunuz : "))

i=0
while(i<adet):
    name = input ("ürün ismi :")
    price = input ("ürün fiyat :")
    urunler.append({
    "name": name,
    "price":price
    })
    i+=1
for urun in urunler :
    print(f"urun adı :{urun['name']} urun fiyatı :{urun['price']}") # burada tek tırnak kullanmak zorundayız.çünkü urun adından başlağımız yerde yani en dışta çift tırnak kullandık
