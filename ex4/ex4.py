#He tret la informació d'aquí
#https://www.pythonpool.com/run-length-encoding-python/

def runlengthencodeing(seq):
    compressed = [] #Creem la llista buida on guardarem la compressió
    count = 1 #Inicialitzem el comptador de caràcters a 1
    char = seq[0] #Inicialitzem la variable 'char' com el primer valor
                  #de la seqüència

    # Fem un for per recorrer tota la seqüència
    for i in range(1, len(seq)):
        #Sumem els caràcters de la seqüència que siguin iguals
        if seq[i] == char:
            count = count + 1
        #Si no són iguals, el caràcter passa a ser el següent i afegim a la
        #llista de compressió el caràcter anterior amb la quantitat.
        else :
            compressed.append([char,count])
            char=seq[i]
            count=1
    #Un cop finalitzat el for, afegim l'últim caràcter amb les vegades que
    #surt repetit a la llista de compressió
    compressed.append([char, count])
    return compressed

def main():
    seq = input('Seqüència:') #Demanem a l'usuari que introdueixi una seqüència
    list = runlengthencodeing(seq) #Cridem a la funció

    compressed_seq = '' #Creem una string buida
    #Fem un for que recorre la llista compressa i la converteix en string
    for i in range(0, len(list)):
        for j in list[i]:
            compressed_seq += str(j)
    print('la seqüència comprimida és: ',compressed_seq)

if __name__=="__main__":
    main()