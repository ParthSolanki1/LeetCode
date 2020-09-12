def blah(a, b):
    x = a
    y = b
    while x != y:
        if(x>y):
            x = x-y
        if(y>x):
            y = y-x
    
    print(y)
    print(x)

blah(2437, 875)
a = "hello"
print(a[0:-1])