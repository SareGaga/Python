def my_decorator(func): # fonksiyona parametre olarak fonksiyon gönderdik
    def wrapper(name):
        print("fonksiyondan önce işlemler")
        func(name)
        print("fonksiyondan sonraki işlemler")
    return wrapper

@my_decorator # sayHello= my_decorator(sayHello) bunu yapmış oluyoruz.
def sayHello(name):
    print("hello",name)

sayHello("ali")

import math
import time

def calculate_time(func):
    def inner(*args,**kwargs):

        start = time.time()
        time.sleep(1) # 1 saniye uyutuyoruz.

        func(*args,**kwargs)

        finish = time.time()
        print("fonksiyon"+func.__name__ +str(finish-start)+"saniye sürdü.")
    return inner

@calculate_time
def usalma(a,b):
    

    print(math.pow(a,b))


@calculate_time  
def faktoriyel(num):

    print(math.factorial(num))


usalma(2,3)