import math

def solution(x1, y1, x2, y2, x3, y3):
    distancia1 = 0
    distancia2 = 0

    auxX=x2-x1
    auxY=y2-y1

    distancia1= math.sqrt((auxX**2)+(auxY**2)) #Calcula la hipotenusa del triangulo

    auxX = x3 - x2
    auxY = y3 - y2

    distancia2 = math.sqrt((auxX ** 2) + (auxY ** 2)) #Calcula la hipotenusa del triangulo


    return ((distancia1+distancia2)/2) #devuelve el promedio

print(solution(0,0,1,1,2,2))