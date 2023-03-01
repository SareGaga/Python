#Yöntem1
# import math # modulü böyle import edebilirz
import math as islem # böylede import edebilirz artık adı islem oldu

# value = dir(math) # math modulün içinde olan şeyleri görürüz
# value=help(math) # modülün yardım dökümanı
# value=help(math.factorial(x)) # faktöriyieldn nasıl kullanıldığına dair bilgi almk istersek

# value = math.sqrt(49)
# value = math.factorial(5)
# value =math.floor(5.9)
# value=math.ceil(5.9)


# value= islem.factorial(5)


# Yöntem2

def sqrt(x):
    print("x :"+str(x)) # bu bir fonk ve eğer üstte yazarsak bunu math kütüphanesindeki sqr ezemez ama importtan sonra yazarsak sqrt methodunu ezer.

# from math import * # math modülünden hepsini(*) import et
from math import factorial,sqrt # sadece iki fonk import ediyoruz burada 

# value =factorial(5)
value = sqrt(9)
print(value)