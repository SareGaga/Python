def not_hesapla(satir):
    satir = satir[:-1]
    liste = satir.split(':')

    ogrenciAdı = liste[0]
    notlar = liste[1].split(",")
    
    not1 = int(notlar[0])
    not2 = int(notlar[1])
    not3 = int(notlar[2])

    ortalama = (not1+not2+not3)/3

    if ortalama>90 and ortalama <=100:
        harf = "AA"
    elif ortalama >= 85 and ortalama<=89:
        harf ="BA"
    elif ortalama >= 65 :
        harf ="CC"
    else:
        harf="FF"

    return ogrenciAdı + ":"+ harf + "\n"
       


def ortalamalari_oku():
   with open("sınav_notları.txt","r",encoding="utf-8") as file:
    for satir in file:
        print(not_hesapla(satir))


def not_gir():
    ad = input("öğrenci adı: ")
    soyad = input("öğrenci soyad: ")
    not1 = input("not 1: ")
    not2 = input("not 2:")
    not3 = input("not 3:")

    with open("sınav_notları.txt","a",encoding="utf-8") as file :
        file.write(ad+"" + soyad + ":"+not1+","+not2+","+not3+"\n")


def notları_kayıtet():
    with open("sınav_notları.txt","r",encoding="utf-8") as file :
        liste = []

        for i in file :
            liste.append(not_hesapla(i)) 
        with open("sonuclar.txt","w",encoding="utf-8") as file2 :
            for i in liste:
                file2.write(i)


while True:
    islem = input ("1- Notları oku\n2- Not git\n3- Notları kayıt et\n4- Çıkış\n")
    
    if islem=="1":
     ortalamalari_oku()
    elif islem =="2":
     not_gir()
    elif islem=="3":
     notları_kayıtet()
    else:
        break