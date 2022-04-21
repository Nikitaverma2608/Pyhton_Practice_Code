#Program to find the factorial os a user defined integer using recursion

def fact(a):
    b=1
    if a ==1 or a==0:
        return 1
    else:
        b = a * fact(a-1)
        return b

val = int(input("Enter a value n : "))

funct_val = fact(val)
print("Factorial of {} is {} ".format(val,funct_val))
