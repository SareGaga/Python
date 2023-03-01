# def changeName(n):
#     n="ada"

# name="sare"

# changeName(name)
# print(name)




# def change(n):
#     n[0] = "istanbul" # listeler refereans tip olduğu için 0 . elamanı değişti
# sehirler = ["ankara","izmir"] 
# n = sehirler[:] # sehirler dizisinin olduğu gibi tüm lemenalarını n ye aktarıyoruz. # slicing

# n[0]="istanbul"

# print(sehirler)
# print(n)




# def change2(n):
#     n[0] = "istanbul" # listeler refereans tip olduğu için 0 . elamanı değişti
# sehirler = ["ankara","izmir"] 

# change2(sehirler[:]) # parçalama işlemi ile kopyasını oluşturduk. Yani referans tip olduğu içi listeler değişir ama value type gibi değişmemesini sağladık.in

# print(sehirler)




# def add (a,b,c=0):
#     return sum((a,b,c))
# print(add(10,20))
# print(add(10,20,50))





# def add2(*params): # böyle yazınca sayı belirtmemiş oluyoruz.
#     print(params)
#     return sum((params))
# print(add2(10,20)) # tuple listesi
# print(add2(10,20,90,41,50,60))





# def add3(*params): # tuple liste türü olduğundan tek yıldız
#     sum = 0
    
#     for n in params:
#         sum = sum + n
#     return sum
# print(add3(10,20)) # tuple listesi
# print(add3(10,20,90))





# def displayUser(**arg): # dictionary liste türü değerler olduğu için iki yıldız konuldu
#     print(type(arg))
#     for key, value in arg.items():
#         print("{} is {}".format(key,value))

# displayUser(name = "sare", age =2, city="istanbul")
# displayUser(name = "ada", age =3, city="kocaeli",phone="54553")
# displayUser(name = "yiğit", age =14, city="ankara",phone="6566", email="yiğit@gmail.com")







def myFunc(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

myFunc(10,20,30,40,50, key1= "value1", key2="value2")

     