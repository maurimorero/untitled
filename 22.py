# -*- coding: utf-8 -*-

def solution (texto):
    indx = 0
    contador = 0
    palabraalreves = invPalabra (texto) # invierte la palabra para hacer la comparación
    bandera=1 # esta bandera se usa para contemplar el caso en que haya solo una letra de diferencia (lo cual implica dos diferencias)

    for i in range (len(texto)):
        if palabraalreves[indx] == texto[indx]:
            indx += 1
            contador += 1
        else:
            if bandera>=0: #chequeo cuantas
                bandera-=1
                indx += 1
                contador += 1
            else:
                return False

    if contador == len(texto): # En caso de que el contador sea igual a la cantidad de letras de la cadena se recorrio el string y es igual (o tiene una letra de diferencia)
        return True

def invPalabra (texto):
    contador = len(texto)
    aux = ""
    indx = -1
    while contador >= 1:
        aux += texto[indx]
        indx -= 1
        contador -= 1
    return aux

print(solution("abcba"))