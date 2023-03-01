class Person():
    def __init__(self,fname,lname):
        self.firstName = fname
        self.lastName = lname
        print("Person Created")

    def who_am_i(self):
        print("I am a person")

    def eat(self):
        print("I am eating")

class Student(Person): # inheritance yaptık
    def __init__(self,fname,lname,number):
        Person.__init__(self,fname,lname) # personın construcotrını eziyor ve bu person çalışması için yazdık.
        self.studentNumber = number

        print("Student Created")

    # ovveride temel sınıftaki methodu ezdi.
    def who_am_i(self):
         print("I am a student")

    def sayHello(self):
        print("hello I am a student")

class Teacher(Person):
    def __init__(self, fname, lname,branch):
        super().__init__(fname,lname) # personın constructorı
        self.branch = branch
    def who_am_i(self):
        print(f"I am a {self.branch} teacher")

p1= Person("ali","yılmaz")
s1 = Student("sare","gaga",1255)
t1 = Teacher("serkan", "yılmaz", "mat")

print(f"{p1.firstName} {p1.lastName}")
print(f"{s1.firstName} {s1.lastName} {s1.studentNumber}")

p1.who_am_i()
s1.who_am_i()
s1.eat()
p1.eat()
s1.sayHello()
t1.who_am_i()