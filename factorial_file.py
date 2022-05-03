def fact(x):
    fact=1
    if x==1 or x==0:
        return 1
    else:
        for i in range(1,x+1):
            fact = fact*i
            
        return fact

user_input=10
y=fact(user_input)
print(user_input,y)
z="factorial of "+str(user_input)+"is "+str(y)

f=open("factorial.txt","w")
f.write(z)
f.write("\n")
f.close()


f=open("factorial.txt","a")
for i in range(5,11):
    y= fact(i)
    print(i,y)
    z="factorial of "+str(i)+" is "+str(y)
    f.write(z)
    f.write("\n")
f.close()

f=open("factorial.txt","w")

data1 = f.read()
print("this is read operation")
print(data1)

f.close()