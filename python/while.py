# 1-100 e kadar

# x = 1
# while x <= 100 :
#     if x % 2 == 1 :
#         print(f"sayı tek :{x}") 
#     else :
#         print(f"sayı çift : {x}")
#     x +=  1
# print("bitti") 



name = "" # False
while not name.strip(): # name True oluncaya dek isminizi giriniz diye sorucak. # strip boşluk değerini siler ve    kullanıcı boşulk değeri bile girse ismini sormaya devam edicek.
    name = input("isminizi giriniz :")

print(f"merhaba , {name}")