website="http://www.sadikturan.com"
course="python kursu: baştan sona python programlama rehberiniz(40 saat)"

#1- 'course' karakter dizisinde kaç karakter bulunmaktadır?

x=course
print(len(x))

#2- 'website' içinden www karakterleini alın.

y=website
print(y[7:10])

# 3- "website" içinden com karakterlerini alın.

y=website
print(y[22:25])
# print(y[length-3:length]) #en sona geldik üç adım geri gittik daha sonra tekrar length yazarak sona gittik

#4- "course" içinden ilk 15 ve son 15 karakterlerini alın.

x=course
print(x[0:15])
print(x[-15:])

#5- "course" ifadesindeki karakterleri tersten yazdırın

x=course
print(x[::-1]) # :: yaparsak tüm karakterleri al deriz ::2 dersek 2şer 2şer al deriz. Tersten almak için -1 diyoruz.

s='12345'*5
print(s[::5]) # sadece 1 değerini 5 kere yazdırıyor.

name,surname,age,job='bora','yılmaz',32,'mühendis'

#6- Yukarıda verilen değişkenler ile ekrana aşağıdaki ifadeyi yazdırın. 'benim adım bora Yılmaz,Yaşım 32 ve mesleğim mühendis'

result=" Benim adım "+ name + " "+ surname+ " , Yaşım "+ str(age)+" ve mesleğim "+ job

print(result)

result2 ='benim adım {} {} ,Yaşım {} ve mesleğim m{}.' .format(name,surname,age,job)

print(result2)

result3 =f'benim adım {name} {surname} ,Yaşım {age} ve mesleğim {job}.'

print(result3)

# 7- 'hello world' ifadesindeki w harfini 'W' ile değiştir.

s='hello world' 
s=s[0:6]+'W'+ s[-4:] # bu birinci yöntem

s.replace('w','W') # bu ikinci yöntem

print(s)

# 'abc' ifadesini yan yana 3 kere yazdır

a ='abc ' *3
print(a)
