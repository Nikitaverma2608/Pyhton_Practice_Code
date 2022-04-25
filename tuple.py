#here id of set will be different 
t1=(1,3,4,5)
t2=(6,8,9)

print(t1)
print(id(t1))
print(t1+t2)
print(id(t1+t2))
print(t1)
print(id(t1))



#here id of a list will be same everytime 
t1=[1,3,4,5]
t2=[6,8,9]

print(t1)
print(id(t1))
 
print(t1+t2) 
print(t1)
print(id(t1))

print(id(t1+t2))

