#to find greater of three number taking values from user

a=int(input("enter first number\n"))
b=int(input("enter second number\n"))
c=int(input("enter third number\n"))

if(a==b==c):
    print("All numbers are equal")
elif(a==b) and (a>c):
    print(a, "and", b ," are equal and greater than ",c )
elif(b==c) and (b>a):
    print(b, "and", c ," are equal and greater than ",a )
elif(c==a) and(c>b):
    print(b, "and", c ," are equal and greater than ",a )
elif(a>b) and (a>c):
    print(a ,"is greater than", b ,"and", c)
elif(b>c) and (b>a):
    print(b ,"is greater than", a ,"and", c)   
else:
    print(c ,"is greater than", b ,"and", a)

    

#a,b,c= int(input("first\n"),int(input("second\n")),int(input("third\n")))    way to take input in a single line of code
    
