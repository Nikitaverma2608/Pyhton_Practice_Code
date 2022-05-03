# A SIMPLE CALCULATOR

print("***** WELCOME TO NIKITA'S CALCULATOR *****")

def Add(x,y):
    return x+y

def Sub(x,y):
    return x-y

def Div(x,y):
    return x/y

def Mult(x,y):
    return x*y

def Mod(x,y):
    return x%y

#If on performing division operation you get error this function will get call
def input_value():
    if(data_typ=="1"):
        num2 = int(input("Enter again the 2nd value : "))
        return num2
    else:
        num2 = float(input("Enter again the 2nd value : "))
        return num2

    
print("1. Integer value.\n2. Float value")

#Taking input from user that which type of value you are going to enter 
data_typ = input("Enter the type of value on which you have to perform operation '1/2' : ")

if(data_typ=="1"):
    num1 = int(input("Enter value 1 : "))
    num2 = int(input("Enter value 2 : "))


    print("***** The operations you can perform *****")
    print(" 1: Addition \n 2: Subtraction \n 3: Multiplication \n 4: Division \n 5: Modulus \n 6: Exponential \n 7. Root ")
        
    #Taking input from user that which operation you want to perform
    opera = int(input("Enter the operation you have to perform 1/2/3/4/5 : "))
    
    if(opera==1):
        a = Add(num1,num2)
        print(num1," + ",num2," = ",a)

    elif(opera==2):
        a = Sub(num1,num2)
        print(num1," - ",num2," = ",a)
            
    elif(opera==3):
        a = Mult(num1,num2)
        print(num1," * ",num2," = ",a)
    
    elif(opera==4):

        #if user enteres num2 = 0 it will give zerodivision error so to handle it writing the following code
        if(num2==0):
            num2 = input_value()
            a = Div(num1,num2)
            print(num1," / ",num2," = ",a)
            #if there is num2 !=0
        else:
            a = Div(num1,num2)
            print(num1," / ",num2," = ",a)
    
    elif(opera==5):
        a = Mod(num1,num2)
        print(num1," % ",num2," = ",a)
            
    else:
        print("Opps! You have entered wrong choice")

elif(data_typ=="2"):
    num1 = float(input("Enter value 1 : "))
    num2 = float(input("Enter value 2 : "))

    print("***** The operations you can perform *****")
    print(" 1: Addition \n 2: Subtraction \n 3: Multiplication \n 4: Division \n 5: Modulus \n 6: Power \n 7: Root")
        
        #Taking input from user that which operation you want to perform
    opera = int(input("Enter the operation you have to perform 1/2/3/4/5 : "))
    
    if(opera==1):
        a = Add(num1,num2)
        print(num1," + ",num2," = ",a)

    elif(opera==2):
        a = Sub(num1,num2)
        print(num1," - ",num2," = ",a)
            
    elif(opera==3):
        a = Mult(num1,num2)
        print(num1," * ",num2," = ",a)
    
    elif(opera==4):
            
        #if user enteres num2 = 0 it will give zerodivision error so to handle it writing the following code
        if(num2==0):
            num2 = input_value()
            a = Div(num1,num2)
            print(num1," / ",num2," = ",a)
            #if there is num2 !=0
        else:
            a = Div(num1,num2)
            print(num1," / ",num2," = ",a)
    
    elif(opera==5):
        a = Mod(num1,num2)
        print(num1," % ",num2," = ",a)

    else:
        print("Opps! You have entered wrong choice")

else:
    print("Opps! You have entered wrong choice")

             

