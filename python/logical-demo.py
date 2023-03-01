
# 1- Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz

a = float(input("sayı :"))

kontrol=(a>0 ) and (a<=100)
print(f"sayı 0 -100 arasında mı : {kontrol}")
# 2- Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz 

a = int(input("sayı :"))
result = (sayı >0) and (sayı % 2 == 0)
print(result)
# 3- Email ve parola bilgiler ile giriş kontrolü yap
email="saregagaa@gmail.com"
password="ab123"

girilenEmail=input("email :")
girilenPassword=input("parola :")

result=(email==girilenEmail) and (girilenPassword == password)
print(resılt)
# 4 - Girilen 3 sayıyı büyüklük olarak karşılaştır

a = int(input("sayı1 :"))
b = int(input("sayı2 :"))
c = int(input("sayı3 :"))

result=(a>b) and(a>c)
print(result)

# 5 - kullanıcıdan 2 vizr(%60) ve final (%40) notunu alıp ortalama hesapla eğer 50 den büyükse geçti


vize1=float(input("1.vize"))
vize2=float(input("2.vize"))
final=float(input("final"))

ortalama=(((vize1+vize2)/2)*0.6)+(final*0.4)

result= (ortalama>=50) and (final>=50)
result= (ortalama>=50) and (final>=70)

print(f" ogrencini ortalmaası :{ortalama} ve geçme durumu {result}")


# 6- kişinin ad, kilo ve boy ile kilo indeks hesapla 

name = input("adınız: ")
kg= float(input("kilonuz: "))
hg=int(input("boyunuz"))

index=(kg)/hg**2
zayif = (index>=0) and (index<=18.4)
normal = (index > 18.4) and (index <=24.9)

print(f"kilo indeksin :{index} ve kilo değerlendirmen zayıf : {zayıf}")

print(f"kilo indeksin :{index} ve kilo değerlendirmen normal : {normal}")
