#To check whether the year is leap or not

year = int(input("enter a year: "))

if((year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0)):   
    print("Given Year is a leap Year")
else:
    print("Given Year is a not leap Year")
