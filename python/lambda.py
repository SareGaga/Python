# def square(num): return num **2

# numbers = [1,3,5,9]

# result = list(map(square,numbers)) # buraya yazarken fonksiyonu çalışturmıyoruz sadece ismini veriyoruz.
# # list yazmamızın nedeni de sonuçları liste şeklinde göstersin diye.
# # map methodunun ya bir listeyle çevriliyor olmalı ya da for döngüsü ile dolaşılması gerekiyor.


# # for item in map (square,numbers):
# #     print(item) #2.yöntem


# print(result)

# yukardaki gibi fonk tanımlamadan lamba ile de yapılır.

square = lambda num : num ** 2
numbers = [1,3,5,9,10,4]

# result = list(map(lambda num : num**2 ,numbers)) # fonksiyon olmadan lambda ile 
# result = list(map(square,numbers)) 
result = square(3)

print(result)


def check_even(num):
    return num%2==0
result2 =list(filter(check_even,numbers)) # filter methodu ile check even fonksyionundaki belirtilen 2 ye bölümünden sıfır kalanları filtreliyor.

# result2 =list(filter(lambda num : num%2==0,numbers))



print(result2)