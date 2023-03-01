# 1- "bmw, mercedes,ople,mazda" elemanlarına sahip liste oluştur

my_list=["bmw", "mercedes","opel","mazda"]

#2- Liste kaç elemanlı

print(len(my_list))

#3- Listenin ilk ve son elemanı nedir

print(my_list[0])
print(my_list[3])
print(my_list[-1])

#4- Mazda değerini toyota ile değiştirin

my_list[-1]="toyota"
print(my_list)

# 5- mercedes listenin bir elemanı mı

result= "mercedes" in my_list
print(result)

#6- Listenin -2 indeksindeki değer nedir.

print(my_list[-2])

#7- listenin ilk 3 elemanını alın

print(my_list[0:3])

#8- Listeinin son 2 elemanı yerine "toyota" ve "renault " değerlerini ekleyin

my_list[-2:]=["toyota", "renault"]
print(my_list)


#9- Listenin üzerine "audi" ve "nissan" değerlerini ekleyin

result3=my_list+["audi","nissan"]

print(result3)

# 10- Listenin son lemanını silin

del my_list[-1]
print(my_list)

# 11- Liste elemanlarını tersten yazdırın

result4= my_list[::-1] # bütün listeyi al en sona git ve ordan başlat
print(result4)

# 12- Aşağıdaki verileri bir liste içinde sakla

studentA= ["yiğit","bilgi",2010,[70,60,70]]
studentB=["sena","turen",199,[80,80,70]]
studentC=["ahmet","turan",1998,[80,70,90]]

result5=studentA[3][1]
print(result5)