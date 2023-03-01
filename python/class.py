# class

class Person :
    # pass # pass burada yer tutucu olarak kullanıldı

    #class attributes
    address = 'no information'

    #constructor(yapıcı method)
    def __init__(self,name,year):
        # object attributes
        self.name = name
        self.year = year
      

    #instance methods
    def intro(self):
        print('hello there '+ self.name)

    def claculateAge(self):
        return 2019 - self.year

    # if a>10:
    #     pass # buraya bir şey yazmak <orundayız yer tutucu olan passı yazabilirz.

#object(instance)
p1= Person(name ='ali',year=1990)
p2 = Person(name='yagmur',year=1995)

#updating
p1.name='ahmet'

#accesing object attributes
print(f"name : {p1.name} year :{p1.year} , address : {p1.address}")
print(f"name : {p2.name} year :{p2.year} , address : {p2.address}")

p1.intro() # methodu çağırıypruz.
p2.intro()

print(f"adım : {p1.name} yaşım : {p1.claculateAge()}")
print(f"adım : {p2.name} yaşım : {p2.claculateAge()}")