import factorial_recursive_method

x = int(input("Enter value of n : "))
y= int(input("Enter value of r : "))    
temp=x-y
fx=factorial_recursive_method.fact(x)
fy=factorial_recursive_method.fact(temp)

permutation= fx/fy

print("Permutation : ",permutation)