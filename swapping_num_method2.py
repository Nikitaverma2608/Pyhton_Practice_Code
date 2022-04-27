#Swapping of two numbers
print("This script is intended to swap the values of two data variable using a third temporary variable!")
a= int(input("enter first integer : "))
b= int(input("enter first integer : "))
print("Values before swapping ")
print("a =", a,"b=",b)

temp=a
a=b
b=temp

print("Values after swapping ")
print("a=",a,"b=",b)
