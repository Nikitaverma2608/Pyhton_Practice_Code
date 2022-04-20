#To find Permutation

n = int(input("Enter value of n : "))
r= int(input("Enter value of r : "))   #no. of item to arrange

#calculate n factorial 
fact=1
for i in range(1,n+1): 
       fact=fact*i

#calculate n-r factorial
d=n-r       
d_fact=1
for i in range(1,d+1):
       d_fact*=i

permutation= fact/d_fact

print("Permutation = ",permutation)




