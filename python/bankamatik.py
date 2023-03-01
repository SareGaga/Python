#bankamatik uygulaması

SadikHesap  = {
    'ad': 'sadık turan',
    'hesapNo':'12565',
    'bakiye':300,
    'ekHesap':2000
}


AliHesap  = {
    'ad': 'ali turan',
    'hesapNo':'12565',
    'bakiye':3300,
    'ekHesap':1000
}


def paraCek(hesap,miktar):
    print(f"Merhaba {hesap['ad']}")

    if (hesap['bakiye']>=miktar):
        hesap['bakiye'] -= miktar
        print("paranızı alabilirsiniz")
    else:
        toplam = hesap['bakiye'] + hesap ['ekHesap'] 

        if (toplam >=miktar):
            ekHesapKullanımı = input("ek hesap kullanılsın mı (e/h)")

            if ekHesapKullanımı == "e":

                ekHesapKullanılacakMiktar = miktar -hesap['bakiye'] 
                hesap['bakiye']=0
                hesap['ekHesap']
                print('paranızı alabilrisniz')
        
            else:
             print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']}")
        else:
            print("üzgünüz bakiye yetersizdir.")

def bakiyeSorgula(hesap):
    print(f"{hesap ['hesapNo']} nolu hesabınızda {hesap['bakiye']} Tl bulunmaktadır . Ek hesap limitiniz ise {hesap['ekHesap']}Tl bulunmaktadır")


paraCek(SadikHesap, 2000)
bakiyeSorgula(SadikHesap)
paraCek(AliHesap , 1000)