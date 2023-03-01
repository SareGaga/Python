ogrenciler={
    "120":{
        "ad":"sare",
        "soyad":"gaga",
        "telefon":"532 65 65 65"
    },
    "125":{
        "ad":"sena",
        "soyad":"gaga",
        "telefon":"532 00 00 00"
    }
}


ogrenciler ={}

number=input("öğrenci no: ")
name=input("öğrenci adı: ")
surname=input("öğrenci soyad: ")
phone=input("öğrenci tel: ")

# ogrenciler[number] = {
#     "ad":name,
#     "soyad":surname,
#     "telefone":phone
# }


ogrenciler.update({
    number:{
        "ad":name,
        "soyad":surname,
        "telefon":phone
    }

})

print(ogrenciler)


ogrNo=input("öğrenci no :")
ogrenci=ogrenciler[ogrNo]

print(f"Aradığınız{ogrNo} nolu öğrencinin adı : {ogrenci['ad']} soyad :{ogrenci['soyad']} ve telefonu ise {ogrenci['telefon']}")
print(ogrenci)