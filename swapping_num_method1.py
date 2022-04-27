#Swapping of two numbers
print("This script is intended to swap the values of two data variable using a third temporary variable!")
a= int(input("enter first integer : "))
b= int(input("enter first integer : "))
print("Values before swapping ")
print("a =", a,"b=",b)

"""method 1
   temp=a;
   a=b;
   b=temp;"""
""" method 2
a=a+b
b=a-b
a=a-b
"""

a,b=b,a
print("Values after swapping ")
#print("a=",a,"b=",b)
print("a = ", str(a))
print("b = ", str(b))



