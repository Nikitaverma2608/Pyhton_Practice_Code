count=1   #global variable : accessible in whole program 

def plus():
    global count
    count += 1

def minus():
    global count
    count -=1

print("count = ",count)
plus()
plus()
minus()
minus()

print("count = ",count)