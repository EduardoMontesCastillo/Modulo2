import sys
def cadena(a):
    a=sys.argv[1] 
    cont=1
    lista=[]
    while cont<a:
        lista.append(cont)
        cont+=1
    return(lista)