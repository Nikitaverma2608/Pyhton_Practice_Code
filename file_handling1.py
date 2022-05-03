
#for writing operation
f= open("My first file.txt","w")

x= "Hello!"
y= "Customer"
f.write(x)
f.write("\n")
f.write(y)

f.close()

#for reading operation
f= open("My first file.txt","r")

y=f.read()
print(y)
f.close()


