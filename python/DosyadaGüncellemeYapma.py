# with open("newfile.txt","r+",encoding='utf-8') as file:
#    file.seek(20) # 20. ci bayta git oraya yaz aşağıdakini diyoruz.
#    file.write("deneme")

# with open("newfile.txt","r+",encoding='utf-8') as file:
#     print(file.read())



# ************ Sayfa Sonunda Güncelleme**********

# with open("newfile.txt","a",encoding="utf-8") as file:
#     file.write("\nEmel Turan")



# ************ Sayfa Başında Güncelleme**********


# with open("newfile.txt","r+",encoding='utf-8') as file:
#    content = file.read()
#    content = "Efe Turan \n"+ content 
#    file.seek(0)
#    file.write(content)
  
 
# ************ Sayfa ortasında Güncelleme********** 


with open("newfile.txt","r+",encoding='utf-8') as file:
    list = file.readlines()
    list.insert(1, "Yılmaz Korkmaz\n") # 1. indexden önce ekle
    file.seek(0) # sayfanın en başından itibaren
    file.writelines(list)
   
    

with open("newfile.txt","r",encoding='utf-8') as file:
   print(file.read())


