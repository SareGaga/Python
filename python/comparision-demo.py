# 1- girilen 2 sayıdan hangisi büyüktür

# a=int(input("a: "))
# b=int(input("b: "))

# result=a>b
# print(f"a :{a} b:{b}den büyüktür : {result}")

# 2 - kullanıcıdan 2 vizr(%60) ve final (%40) notunu alıp ortalama hesapla eğer 50 den büyükse geçti

# vize1=float(input("1.vize"))
# vize2=float(input("2.vize"))
# final=float(input("final"))

# ortalama=(((vize1+vize2)/2)*0.6)+(final*0.4)

# print(f"not ortalamanız :{ortalama} ve dersten geçme durmunuz :{ortalama>=50}")


#3- girilen bir sayının tek mi çift mi olduğunu yazdırın 

# sayı=int(input("sayı :"))

# tekcift= (sayi %2 == 0)

# print(f" girilen sayı çift olma durumu : {tekcift}")

# 4- Girilen bir sayının pozirtif mi negatif mi

# sayi = int(input("sayı :"))

# pozitifmi=(sayi>0)
# print(f"girilen sayının pozitif olma durumu {pozitifmi}")

# 5 - parola ve eamil isteyip doğruluğunu kontrol et

email="saregagaa@gmail.com"
password="ab123"

girilenEmail=input("email :")
girilenPassword=input("parola :")

isEmail=(email==girilenEmail.lower().strip()) # lower methodu girilen karakter büyükse küçültüyor strip ise parola ve mail girerken bırakılan boşlukları siliyor.

isPAssword=(password==girilenPassword.lower())

print(f"Email bilgisi doğrumu :{isEmail} ve parola doğru mu :{isPAssword}")