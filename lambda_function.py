'''x = lambda x,y:x+y
print(z(2,4))'''
'''
def even(n):
    return n%2==0   #return boolean values


list1=[2,13,42,4,524,331,452,321,22]

list_even =[]
print(list1)
print(list_even)

for i in list1:
    y = even(i)
    if y==True:
        
    #if i%2==0:
        list_even.append(i)
print(list_even)'''

'''list having negative n positive values we have to filter negatives values then convert negative
by positive with map function then sum of negative values'''

#An anonymous function is a function that is not stored in a program file, but is associated with a variable whose data type is function_handle 
'''
def even(n):
    return n%2==0  '''
from functools import reduce

list1=[2,13,42,4,524,331,452,321,22]
#list_even = list(filter(even,list1))#take two parametres 1.functions
list_even =list(filter(lambda x:x%2==0,list1))
list_even =filter(lambda x:x%2==0,list1)
print(type(list_even))
list_odd = list(filter(lambda x:x%2!=0,list1))

print(list1)
print(list_even)
print(list_odd)

list_even2 = list(map(lambda x:x*2,list_even))
print(list_even2)


sum=reduce(lambda x,y:x+y,list_even2)
print(sum)