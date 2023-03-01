# key - value

sehirler = ["kocaeli" , "istanbul"]
plakalar=[41,34]

print(plakalar[sehirler.index(("kocaeli"))])

# print(plakalar["kocaeli"]) => 41

plakalar = {"kocaeli" : 41, "istanbul" : 34}
print(plakalar["kocaeli"])


plakalar["ankara"] = 6  # ankarayı ekliyoruz.
plakalar["ankara"] = "new value"




print(plakalar)


users={
    "sare":{
        "age": 22,
        "email": "saregagaa@gmail.com",
        "roles":["admin","user"]


    },
    "sena" :{
        "age": 26,
        "roles":["admin","user"]
    }
}

print(users["sare"])
print(users["sare"]["roles"][0])
print(users["sena"]["age"])

