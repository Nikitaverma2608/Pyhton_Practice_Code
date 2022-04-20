#To find the area and circumference of the circle

def circle(x):
    area = 22/7 * x * x
    circum = 2 * 22/7 * x
    return area, circum

r = int(input("Enter the radius of circle : "))
a,b=circle(r)

print("Area of circle is ",a)
print("Circumference of circle is ",b)

# a=5
# area= 22/7*a*a 
# print(area)
# area = round(area,3)
# print(area)