#Swapping of two numbers
print("This script is intended to swap the values of two data variable using a third temporary variable!")
a= int(input("enter first integer : "))
b= int(input("enter first integer : "))
print("Values before swapping ")
print("a =", a,"b=",b)

a=a+b
b=a-b
a=a-b

print("Values after swapping ")
print("a=",a,"b=",b)
