
prueba= [20,17,18, 17, 17, 17, 20, 17, 18,18, 18, 18, 19, 18, 17, 18, 18, 21,18]

def media_aritmetica(prueba):
    promedio= len(prueba)
    indice= 0
    media= 0
    while indice < promedio:
        media+= prueba[indice]
        indice+= 1
    result= media/promedio
    return result

def mediana(prueba):
    muestra= sorted(prueba)
    ind= 0
    while ind < len(prueba):
        if len(muestra)%2!= 0:
            posic= len(muestra)//2
            mediana= muestra[posic]  
        else:
            posicion= (len(muestra)//2) 
            mediana= (muestra[posicion] + muestra[posicion +1])/2
            
        ind+=1
    return mediana
            
def moda(prueba):
    indice= 0
    mapa= {}
    maximo=0
    elemento= 0
    while indice < len(prueba):
        if prueba[indice] in mapa:
            mapa[prueba[indice]]+=1
        else:
            mapa[prueba[indice]]= 1
        indice+= 1
    for llave, valor in mapa.items():
        if valor > maximo:
            maximo= valor
            elemento= llave
    return elemento

def desviacion_estandar(muestra,miu):
    res=0
    for elemento in muestra:
        res+=(elemento- miu)**2
    return math.sqrt(res/(len(muestra)-1))
 

