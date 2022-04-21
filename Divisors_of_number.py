#Program that asks the user for a number and then prints out a list of all the divisors of that number

num = int(input("Enter a number to print its divisor : "))

print("All Divisor of ",num ,"is : ")
for i in range(1,num+1):
    if num%i==0:
        print(i)
        i+=1
