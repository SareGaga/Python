x,y,z =2,5,10
numbers=1,5,7,10,6

#1- kullanıcıdan aldığınız 2 sayının çarpımı ile x,y,z toplamının farkı nedir

# a=int(input("birinci sayı"))
# b=int(input("ikinci sayı"))
 
# result= (a*b) - (x+y+z)
# print(result)

#2- y nin x e kalansız bölümünü hesapla

# result = y//x
# print(result)

# 3- (x,y,z) toplamının mod 3 ü nedir

# result=(x+y+z)%3
# print(result)

# 4 - y nin x inci kuvvetini hesapla

# result = y**x
# print(result)


# 5- x, *y,z = numbers işlemine göre z nin küpü
numbers=1,5,7,10,6

x,*y,z=numbers
result=z**3
print(result)

# 6 - x,*y,z =  numbers işlemine göre y nin değerleri  toplamı 

numbers=1,5,7,10,6
x,*y,z=numbers

result= y[0]+y[1]+y[2]
print(result)