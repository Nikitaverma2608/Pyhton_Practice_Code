from numpy import *
#2-D array
x = array([[1,2,3,4,5],[3,4,5,6,7]])
print(x)
print(type(x))

print(x[1,2])

#3-D array
x = array([
        [[1,2,3,4,5],[3,4,5,6,7],[5,7,8,9,0]],
        
          [[89,56,44,33,22],[65,98,75,63,22],[34,56,78,98,4]]
         ])

print(x)
print(type(x))

print(x[1,2,3])