numero = int(input("Introduce un numero: "))
print ("El numero que ingreso es:\n",numero)


f = open ('holamundo.txt','w')
f.write('SOS ALTO SEEEEEEEEEEEEEEEEER')
f.close()


def checkPostCodeUK(code):
    if (len(code)<6)or(len(code)>8):
        return 0
    parts= code.split()
    #print (len(parts))
    #print(len(parts[0]))
    outward= parts[0]
    inward = parts[1]
    if (len(outward)<2)or(len(outward)>4):
        return 0
    if (len(inward)!=3):
        return 0
    print(outward.isalpha())
    print(inward.isalpha())