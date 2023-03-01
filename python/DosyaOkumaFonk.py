with open("newfile.txt","r",encoding='utf-8') as file:
    content =file.read()
    print(content)
    input()
    file.seek(0) # seek  kürsörün tekrardan nereye gitmesini sağlıyor 0 dedik yanı başa geri dönsün
    print(file.tell()) #kürsörün konumunu verir.
    content2 = file.read()
    print(content2)

   
# with ile oluşturduğumuz kod bloğunun sonuna geldiğimiz zaman otomatik olarak dosya kapanacak o yüzden file.close() yazmadık


