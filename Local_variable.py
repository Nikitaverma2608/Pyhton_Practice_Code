def user_input():
    a = int(input("Enter value 1 "))   #local variable : accessible to function only
    b = int(input("Enter value 2 "))  
    return(a,b)

def add(a,b):
    return a+b

a,b=user_input()
print(a,'+',b, '=',add(a,b))
   