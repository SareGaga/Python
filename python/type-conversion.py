"""
x = input("1 sayı:")
y = input("2. sayı :")

print(type(x))
print(type(y))

toplam=int(x)+int(y)

print(toplam)
"""


x=5
y=2.5
name="çınar"
isOnline=True

# print(type(x))
# print(type(y))
# print(type(name))
# print(type(isOnline))


#Type Conversion

# int to float

# x = 5
# x = float(x)
# print(x)
# print(type(x))

#float to int

# y=int(y)
# print(y)
# print(type(y))

# result = str(x)+str(y)
# print(result)
# print(type(result))


#bool to str

# isOnline = str(isOnline)
# print(isOnline)
# print(type(isOnline))

#bool to int

# isOnline=False
# İsOnline = int(isOnline)
# print(isOnline)
# print(type(isOnline))


pi=3.14
r1= float(input("yarı çap :")) # burada tipleri float yaptık

alan= pi *( r1 **2) #daire alanı
cevre= 2 * pi * r1  #çevre

print("alan : " + str(alan) + " çevre : "+ str(cevre)) # yazdırması için tipi string diye burada değiştirmeliyiz
print(type(alan))
# print("çevre :", cevre ) 
