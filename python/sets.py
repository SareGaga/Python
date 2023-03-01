fruits={'orange','apple','banana'}

#print(fruits[0]) # bu liste indekslenemez 



for x in fruits:
    print(fruits)

fruits.add("cherry") # liste içinde bir elemandan sadece bir tane olur. add methoduyla ekleme çalışırsak eklenmez ya da update ile

fruits.update(["mango","grape"])
print(fruits)

myList=[1,2,3,5,6,5]

print(set(myList)) # set tekrarlayan elemanları listeden çıkarır.

fruits.remove("mango")
fruits.discard("apple") # remove ile aynı siliyor.

fruits.pop() #  indekslenen bir listede pop listenin sonundakini siliyordu ancak fruits indekslenen bir liste değil o yüzden pop herhangibir elemanı siler.



fruits.clear()
