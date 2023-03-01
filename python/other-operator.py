# Identity operator : is

x = y = [1,2,3]
z = [1,2,3]

print(x==y)
print(x==z)
print( x is y) # true
print( x is z) # false çünkü objelerin aynı mı değil mi diye sorguluyor x ve z nin değerleri önemli değil adresine bakıyor ve ikisi farklı adreslere sahip.and
print( x is not y)






# Membership operator : in

x = ["apple","banana"]
print("banana" in x) # banan x listesinde var mı

name = "sare"
print("a" not in name)