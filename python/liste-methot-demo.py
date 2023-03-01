names=["ali","yağmur","hakan","deniz"]

years = [1998,2000,1998,1987]

#1- "cenk" ismini liste sonuna ekle

# names.append("cenk")
# print(names)

# 2- "sena" değerini listenin başına ekle

# names.insert(0,"sena")

# print(names)

#3- "deniz" değerini listeden sil

# names.remove("deniz")
# print(names)


#4- "deniz" isminin index nedir ?

# print(names.index("deniz"))

#5- "ali" listenin bir elemanı mı 

# result="ali" in names
# print(result)

#6- Liste elemanlarını ters çevirin

names.reverse()
print(names)

#7- Alfabetik sıralama
names.sort()
print(names)

#8- yerası büyükten küçüğe sırala

# years.sort()
# print(years)

# #9- str="chevrolet,Dacia" karakter dizisini listeye çevir
# str="chevrolet,Dacia"
# result = str.split(',') # virgül ile ayrıldın
# print(result)

#10- years sizinin ne büyük ve en küçük lemean nedir

# min = min(years)
# max= max(years)
# print(min,max)

#11- years dizisinde kaç tane 1998 değeri var

# result4=years.count(1998)
# # print(result4)

#12- years dizisinin tüm elemanlarını siliniz.

# years.clear()
# print(years)

#13- kullanıcıdan laacağınız 3 tane marka bilgisini listede sakla

markalar=[]

marka= input("marka :")
markalar.append(marka)

print(marka)