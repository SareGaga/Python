# error => hata

#
# print(a) => NameError
#int('1a2') => ValueError
# print(10/0) => zerDivisionError
#print('deneme'e)=> SyntacError



#error handling => hata yöntemi


# try:
#     x = int(input('x :'))
#     y = int(input('y :'))
#     print(x/y)

# except (ZeroDivisionError,ValueError) as e: # hatalara takma isim taktık e diye
#     print("yanlış bilgi girdiniz.")
#     print(e)



# try:
#     x = int(input('x :'))
#     y = int(input('y :'))
#     print(x/y)

# except : 
#     print("yanlış bilgi girdiniz.")
   

    


while True:
    try:
        x = int(input('x :'))
        y = int(input('y :'))
        print(x/y)
    except Exception as a: # except classını inheritance yapıyoruz bu sayede hata ne ise yazıyor
        print('yanlış bilgi girdiniz.',a)
    else:
        break
    finally :
        print("try except sonlandı.")