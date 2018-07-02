# -*- coding: utf-8 -*-
# Se pone la línea de arriba para que se incluyan acentos y la letra ñ

def IsCasiPalindromo (texto):
    # invierto el orden de la palabra para hacer comparación
    contador = len(texto)
    aux = ""
    indx = -1
    while contador >= 1:
        aux += texto[indx]
        indx -= 1
        contador -= 1
    palabraalreves=aux
    indx = 0
    contador = 0

    bandera=1 # esta bandera la uso para contemplar el caso en que haya solo una letra de diferencia (lo cual implica dos diferencias en la comparación)

    for i in range (len(texto)):
        if palabraalreves[indx] == texto[indx]:
            indx += 1
            contador += 1
        else:
            if bandera>=0: # chequeo cantidad de diferencias
                bandera-=1
                indx += 1
                contador += 1
            else:
                return False

    if contador == len(texto): # en caso de que el contador sea igual a la cantidad de letras de la cadena se recorrio el string y es igual (o tiene una letra de diferencia)
        return True


print(IsCasiPalindromo("abccfg"))