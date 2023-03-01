# girilen sayının asal olup olmadığını bulun.
# asal sayı 1 ve kendisi hariç tam böleni olmayan sayılara denir.


sayı = int(input ("sayı :"))
asalmı = True

if sayı == 1 :
    asalmı = False
   

for i in range (2,sayı):
    if (sayı % i == 0 ):
        asalmı = False
        break
        
if asalmı:
    print("sayı asaldır")
else :
    print("sayı asal değildir")

