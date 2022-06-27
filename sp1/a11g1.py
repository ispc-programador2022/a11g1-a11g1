# App A11G1

# Importamos la función bienvenida
from funciones.bienvenida import bienvenida
from funciones.ing2i import ing2i
from funciones.ing2s import ing2s
from funciones.resta import resta
from funciones.potencia import potencia
from funciones.p1sum import p1sum



bienvenida()

enteros = ing2i()
print('Los enteros intresados son: ', enteros[0], enteros[1])

cadenas = ing2s()
print('Los strings intresados son: ', cadenas[0], cadenas[1])