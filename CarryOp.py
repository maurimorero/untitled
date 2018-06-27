def solution(A, B):
    a=str(A)
    b=str(B)
    primero=[]
    segundo=[]

    for valor in a:
        #print (valor)
        primero.append(valor)

    for valor in b:
        #print (valor)
        segundo.append(valor)

    flag=0
    carries=0
    aux = 0
    while (flag==0):
        #print ("aca! - "+ str(len(primero))+" - "+str(len(segundo)))
        valor1= int(primero.pop())
        valor2= int(segundo.pop())

        if((valor1+valor2+aux) >9):
            carries+=1
            aux=1
        else:
            aux = 0
        if(len(primero)==0) or (len(segundo)==0):
            flag=1
            #print("ESTOY ACAAAAAA")

    return carries

print (solution(11111111111156,0))