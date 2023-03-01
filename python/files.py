# Dosya açmak ve oluşturmak için open() fonk kullanılır.
#kullanımı : open(dosya_adi,dosya_erişme_modu)
#dosya_erişme_modu => dosyayı hangi amaçla açtığımızı belirtir.

#"W": (Write) yazma modu. Dosya konumda oluşturur.
# Dosya içeriğini siler ve yeniden ekleme yapar.

# file = open("newfile.txt","w")
# file.close()

# file = open("c:/users/asus/desktop/newfile.txt","w") 
# # başka dizinde dosya oluşturma
# print(file)

# file = open("newfile.txt","w",encoding='utf-8') # türkçe karakteri tanısın diye encodingi verdik
# # file.write("sare gaga")
# file.close()    



#"A": (Append) ekleme. Dosya konumda yoksa oluşturur.
# "w" modundaki gibi içerik silinmez var olan içeriğin üstüne ekleme yapar.

# file = open("newfile.txt","a",encoding='utf-8')
# file.write("\n sare gaga") # ters slaşla yazınca alt satıra geçiyor.
# file.write("sare gaga\n")
# file.close()



# "x" (create) oluşturma. Dosya zaten varsa hata verir.

# file = open("newfile2.txt","x",encoding='utf-8')


#"r"(read) okuma. Varsayılan dosya konumda yoksa hata verir.


# try:
#     file = open("newfile3.txt","r")
#     print(file)
# except FileNotFoundError:
#     print("dosya okuma hatası")
# finally:
#     print("dosya kapandı")
#     file.close()    

# *****************read fonksiyonu

file = open("newfile.txt","r",encoding='utf-8') 

# # for dongüsü
# for i in file:
#     print(i,end="") # end yazdık boş satır eklememesi için 


#read() fonk

# content1 = file.read()

# print("içerik1")
# print(content1)

# content2=file.read()

# print("içerik2")
# print(content2)


# content=file.read(5) # ilk beş karakteri al demek
# print(content)





# *****************readline fonksiyonu

# print(file.readline(),end ="")  # her defasında bir satır okur
# print(file.readline(),end ="")




# *****************readlines() fonksiyonu
liste = file.readlines() # her satırı liste elemanı olarak gösterir
print(liste)
# print(liste[3])

file.close()