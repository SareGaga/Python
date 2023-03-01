website= "http://www.sadikturan.com"

course= "python kursu: baştan sona python programlama rehberiniz(40 saat)"

# 1- ' Hello World ' karakter dizisinin baş ve sondaki boşluk karakterlerini silin.

result=' Hello World '.strip() 
result=' Hello World '.lstrip()  #sadece soldan silmek için.
result=' Hello World '.rstrip() #sadece sağdan silmek için.

result=website.lstrip('/:pth') # sileceğimiz karakterleri de belirtebiliyoruz.

#2-  "http://www.sadikturan.com" içindeki sadikturan bilgisi haricindeki her karakteri sil

result="http://www.sadikturan.com".strip("W.moc")



# 3- 'course ' karakter dizisindeki tüm karakterleri küçük harf yapın.

result=course.lower()

#4-'website' içindeki kaç tane a karakteri var ?

result= website.count('a')
result= website.count('www',0,10) # 0dan 10 a kadar ara

# 5- 'website' WWW ile başlayıp com ile bitiyor mu

result=website.startswith('www')
result=website.startswith('http')
result=website.endswith('com')

# 6- 'website' içinde '.com' ifadesi var mı

result=website.find('.com') # bulduğunun index numarasını döndürüyor.
result=website.find('.com',0,10) # 0 ile 10. index arasında bu değer var mı 

result=course.rfind('python') # sağdan saymaya başla.

#7- 'course' içindeki karakterlerin hepsi alfabetik mi

result= course.isalpha()
result='Hello'.isalpha()
result=course.isdigit() # ifadeler rakam mı 


#8- 'contents ' ifadesindeki satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyiniz.

result='contents'.center(50,'*')

result='contents'.ljust(50,'*') # ifadeyi sola yaslar.

result='contents'.rjust(50,'*') # ifadeyi sağa yaslar.



#9- 'course' karakter dizesindeki boşluk karakterlerini * ile değiştir.

result=course.replace(' ', '-',5) # 5 ile sınırını belirttik

result=course.replace(' ', '') # boşluklar sil


#10- 'hello word' karakter dizisindeki 'world' ifadesini 'there' olarak değiştirin

result='hello word'.replace( 'world' , 'there' )

# 11- 'course' karakter dizisinin boşluk karakterlerinden ayırın


result=course.split(' ')
result=result[2]

print(result)