print("String reversal using swapping")
a=input("Enter a string : ")
x=len(a)
print("String after reversing")
for i in range(x-1,-1,-1):
    print(a[i], end="")
