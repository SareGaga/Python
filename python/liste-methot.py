numbers=[1,10,3,5,6,5,5]
letters= ["a","g","s","b"]

val=min(numbers)
val=max(numbers)


print(val)

val = numbers[3:6]
val = numbers[:3]
val = numbers[4:]

numbers[4]=40
print(numbers)

numbers.append('49') # bu şekilde listeye eleman ekleyebilriz.

numbers.insert(3,78) # istedğimiz yere eleman eklmeke için indexi kullanırız 3. elemandan sonra 78 i ekle diyoruz.and

numbers.insert(-1,52)

numbers.pop() # listedeki elemanları siler parantez içine istediğimiz elemanını index yazabiliyoruz.

numbers.pop(-1)

numbers.remove(49) # 49 u bul ve sil 


numbers.sort() # liste sayısal büyüklük olarak sıralanır.

letters.sort() # alfabetik sıraladı

numbers.reverse()# listeyi ters çevirir.


print(len(numbers))


print(numbers.count(10))   # 10 rakamı kaç tane olduğunu sayar

numbers.clear() # tüm elemanları siler.
print(numbers)
