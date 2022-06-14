import random

def genrnd():
    lista= []
    for i in range(0,50):    
        i = random.randint(0,50)
        lista.append(i)
    return(lista)
    
genrnd()
