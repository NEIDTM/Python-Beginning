import random

def my_de():

    list = []
    
    x = 0

    while x < 50:
        x = x + 1
        list.append(x)  

    z = random.choice(list)
    print(z)

    while z != 1:
        z = random.choice(list)
        print(z)
        if z == 1:
            print('You have got the correct number')

my_de()