numbers =[1,2,3,4,5]

for a in numbers :
    print("hello")


names =["çınar","sare"]
for name in names:
    print(f"my name is {name}")


name="sare gaga" # her bir karakter bir dizi elemanı gibi belirleniyor 
for n in name:
    print(n)


tuple=[(1,2),(3,4),(5,6)]

for a,b in tuple:
    print(a,b)


d = {"k1" :1, "k2" :2, "k3" : 3} # dictionary listesi

# for item in d :   # listenin içindeki sadece key bilgilerini çıkartıcak

# for item in d.items(): # listenin içindeki value değerlerine ulaşmak için böyle yazmalıyız.

for key,value in d.items():
    print(value)