from time import *
x1=time()
print(x1)
num = int((input("Enter a number to print its factorial : ")))

fact=1
if num ==1 or num == 0:
    fact= 1
else:    
    for i in range (1,num+1):
          fact=fact*i

print("Factorial of ", num , "is" , fact)

x2=time()
print(x2)