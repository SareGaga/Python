def toplama(a,b):
    return a+b
def cıkarma(a,b):
    return a-b
def carpma(a,b):
    return a*b
def bolme(a,b):
    return a/b  

def islem(f1,f2,f3,f4,islem_adı):
    if islem_adı=="toplama":
        print(f1(2,3))
    elif islem_adı=="cıkarma":
        print(f2(5,3))
    elif islem_adı=="carpma":
        print(f3(3,4))
    elif islem_adı =="bolme":
        print(f4(10,2))
    else:
        print("geçersiz işlem...")

        
islem(toplama, cıkarma, carpma, bolme, "toplama")   
islem(toplama, cıkarma, carpma, bolme, "cıkarma")   
islem(toplama, cıkarma, carpma, bolme, "carpma")   
islem(toplama, cıkarma, carpma, bolme, "bolme")   
islem(toplama, cıkarma, carpma, bolme, "çarpmaa")   