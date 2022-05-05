def avg(*value):
    x=0
    for i in value:
        x=x+i
    return x/len(value)

y=avg(3,6,9)

print(y)