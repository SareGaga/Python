# RANGE methodu

# for item in range(2,10,5): # range döngü methodudur ve 2den  10 a kadar 5 er 5er artsın demektir
#     print(item)

# print(list(range(2,10,5))) # listeye çeviriyoruz 



# Enumerate : index numarasını verir ve listeler.


# greeting ="hello there"

# for index,letter in enumerate(greeting) :
#     print(f"index : {index} letter : {letter}")
#     index += 1



# zip  : iki listeyi birbirleriyle eşleştiriyor.

list1 = [1,2,3,4,5]
list2= ["a","b","c","d","e"]

print(list(zip(list1,list2)))

for item in zip(list1,list2):
    print(item)

for a,b in zip(list1,list2):
    print(a)