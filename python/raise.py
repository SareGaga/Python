# x = 10

# if x>5:
#     raise Exception("x 5 den büyük değer alamaz")






# def check_password(psw):
#     import re
#     if len(psw) < 8:
#         raise Exception("parola en fazla 7 karakter olmalı") # raise hatayı fırlatıyor.
#     elif not re.search("[a-z]",psw):
#         raise Exception("parola küçük harf içermelidir.")
#     else:
#         print("geçerli parola")

# password="12345678"

# try:
#     check_password(password)
# except Exception as ex:
#     print(ex)
# else:
#     print("geçerli parola : else")
# finally :
#     print("validation tamamlandı")







class Person:
    def __init__(self,name,year):
        if len(name)>10:
            raise Exception("name alanı fazla karakter içeriyor.")
        else:
            self.name=name # eğer name alanı fazla karakter içermiyorsa set ediyor.

p=Person("Aliiiiiiiiiiiiiiiii",1989)
