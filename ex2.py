import sys

def cadena(a):
    #a=int(input("Ingrese numero:")) 
    cont=1 #Se inicia un contador en 1
    lista=[] #Se inicia una lista vacia 
    while cont<=a: #Mientras el contador sea menor o igual al argumento, se ejecuta el while
        lista.append(cont) #Se agrega el valor del contador a la lista
        cont+=1 #Se suma uno al contador
    return(lista) #Se devuelve el contenido de la lista

print(cadena(int(sys.argv[1] ))) #Se ingresa un numero como argumento para la funcion
    
def primos(n):
    lista_primos=[] #Se inicia una lista vacia
    if n > 0: #El argumento debe ser mayor a cero
        for i in range(2,n): #Se ejecuta un ciclo en un rango de 2 a n
            num=2 #Se establece una variable bandera
            Primo=True #Se establece una variable bandera como true
            while Primo and num<i: #Mientras se este en el rango de 2 menor a i
                if i % num == 0: # Si el sobrante de la division de i entre 2 es igual a cero no es primo 
                    Primo=False
                else: #Sino se agrega el numero a la lista de primos
                    num+=1
            if Primo:
                lista_primos.append(i) #Si primo es true se agrega i a la lista.
    return (lista_primos)            
            
print(primos(int(sys.argv[1] ))) #Se ingresa un numero como argumento para la funcion y se manda a hablar a la funcion, regresando el return de lista_primos
