import sys

def cadena(a):
    numero=0
    a=(sys.argv) 
    while a > numero:
        print(numero)

def primos(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        
        return True

n = len(sys.argv)
for i in range(1, n):
    print(i, primos(i))
