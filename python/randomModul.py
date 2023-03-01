import random #  dosyanın ismi modül ismi ile aynı olmamalı !!

# result = dir(random) # random modülünün içinde kullanabileceğimiz methotları gösterir.

# result = random.random() #0.0 - 1.0 arasında random sayı üreticek
result2 = random.random()*100
result3 = int(random.uniform(10, 100)) # 1 ile 10 arasında rastgele sayı üretir
# int içine almamızdaki yararda virgülden sonrasını göstermez sadece tam ksımını bize gösterir.

result4= random.randint(1, 100) # randomint ile int yazmdan tam ksımını gösterir

names=["ali","yagmur","deniz","sare"]
# result= names[random.randint(0,len(names)-1)] #1.yöntem
result = random.choice(names) #2.yöntem choices adında methodu kullanabilirz.

greeting ="hello there"
result5=random.choice(greeting)

liste = list(range(10))
random.shuffle(liste)
result6=liste


liste2=range(100) # bunu listeye çevirmedik !!
result7=random.sample(liste, 3) # listenin içinden 3 tane rastgele sayıyı liste halinde getiriyor.
result8=random.sample(names, 3)

print(result)
print(result2)
print(result3)
print(result4)
print(result5)
print(result6)
print(result7)
print(result8)