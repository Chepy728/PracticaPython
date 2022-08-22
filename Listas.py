#!/usr/bin/python

lista = [1,-5,6,78,9,33]

def mayor (lista):
    
        max = lista[0]
        for x in lista:
            if x > max:
                max = x
        return max

def menor (lista):
    
        min = lista[0]
        for x in lista:
            if x < min:
                min = x
        return min

print("La lista es:",lista)
print("El mayor de la lista es:",mayor(lista))
print("El mayor de la lista es:",menor(lista))




