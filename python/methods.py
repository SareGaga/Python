#method # method bir sınıf üyesi

list=[1,2,3,4]

list.append(4)
print(list)
print(type(list))

myString="hello"
print(myString.upper())
print(type(myString))

# fonksiyon 

def sayHello(name="user"): 

    print("hello "+ name)

sayHello("sare") # fonksiyonu çağırdık # name parametresini verdik
sayHello() # parametre göndermez isek yukaradki user atanır


def sayHello2(name):
    return "hello" + name
msg = sayHello2("sena")
print(msg)


def total(num1,num2):
    return num1+num2
result=total(10, 20)
print(result)


def yasHesapla(dogumYılı):
   return 2023 - dogumYılı
ageSare = yasHesapla(2001)
print(ageSare)


def EmekliligeKaçYılKaldı(dogumYılı,isim):
    '''
    DOCSTRING : doğum yılınıza göre emekliliğinize kaç yıl kaldı
    input : doğum yılı
    output : hesaplanan yıl bilgisi

    '''
    yas = yasHesapla(dogumYılı)
    emeklilik = 65 - yas

    if emeklilik > 0 :
        print(f"emekliliğinize {emeklilik} yıl kaldı")
    else:
        print("zaten emekli oldunuz")
    
EmekliligeKaçYılKaldı(1983, "Ali")


print(help(EmekliligeKaçYılKaldı)) # fonkisyonun kullanım şeklini öğrenmek için yazıyoruz.




list = [1,2,3,0]

print(help(list.append))