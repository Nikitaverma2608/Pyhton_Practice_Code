#Program to print fibonacci series
from time import * 
x1= time()
print(x1)
num = int((input("Enter a number to print fibonacci series till that term : ")))
a=0
b=1

print("Fibonnacci series upto ", num, "term is :")
if num<=0:
    print("Enter a positive integer.")
elif num==1:
    print(num)
else:
    for i in range(0, num):
          sumi = a+b
          print(sumi)
          a=b
          b=sumi
    
x2= time()
print(x2)   
    
