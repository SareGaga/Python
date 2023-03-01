 #fonksiyondan geriye bir değer değilde fonksiyon döndüreceğiz
def usalma(number):
    
    def inner(power):
        return number ** power
    return inner # inner() yazıp fonksiyonu çağırmadık fonksiyonu döndürdük.

two = usalma(2)
print(two(3)) # 2 üzeri 3 oluyor.



# def yetki_sorgula(page):
#     def inner(role):
#         if role == "Admin":
#             return "{0} rolünün {1} sayfasına ulaşabilir.".format(role,page)
#         else :
#              return "{0} rolü {1} sayfasına ulaşamaz.".format(role,page)
#     return inner
# user1 = yetki_sorgula("product edit")
# print(user1("Admin"))
# print(user1("user"))


def islem(islem_adı):
    def toplam(*args):
        toplam =0
        for i in args:
            toplam+=i
        return toplam
    def carpma(*args):
        carpim = 1
        for i in args:
            carpim*=i
        return carpim
    if islem_adı=="toplama":
        return toplam
    else:
        return carpma

toplama = islem ("toplama")
print(toplama(1,3,5,5,9,5))

carpma = islem("carpma")
print(carpma(1,5,9,4,3,))