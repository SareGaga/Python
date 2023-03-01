#global scope
x = "golbal x"

def function ():
    # local scope 
    x = "local x"
    print(x)

function()
print(x)

######################

#global
name ="ada"

def changeName(new_name):
    #local
    name = new_name
    print(name)

changeName("sare")
print(name)

######################

name = "global string"

def greeting():
    name="sare"

    def hello():
        name="ada"
        print("hello"+name)

    hello()
greeting()

######################

x = 50
def test():
    global x
    print(f"x: {x}")

    x=100
    print(f"changed x to {x}")

test()
print(x)