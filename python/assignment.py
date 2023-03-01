# x=5
# Y=10
# z=20

# x,y,x = 5,16,20

# x,y =y,x
# x= x+5
# x+=5  # x=x+5
# x-=5
# x*=5
# x/=5
# x%=5
# y//=5  # y = y//5 bölümün sadece tam kısmını alır
# y**=5  # y=y**5
# y**=z

values =  1,2,3,4,5 #tuple listemiz
print(type(values))

x,y,*z=values # z nin başındaki yıldız 3,4,5 i liste şeklinde z ye atar. 

print(x,y,z[0])
