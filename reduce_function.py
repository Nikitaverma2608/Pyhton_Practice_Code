from functools import reduce

x = [1, 2, 3, 4]
a=reduce( (lambda x, y: x * y), x )
print(a) 