from unicodedata import decimal

if __name__ == '__main__':
    #Tipos de datos básicos

    entero = 42                         #int
    decimal = 3.14                      #float
    complejo = 2 + 3j                   #complex
    booleano = True                     #bool
    cadena = "Hola, Python!"            #str
    binario = bytes([50, 100, 150])     #bytes


    print("Tipos básicos:")
    print("Entero:", entero)
    print("Decimal:", decimal)
    print("Complejo:", complejo)
    print("Boooleano:", booleano)
    print("Cadena:", cadena)
    print("Binario:", binario, "\n")

    #Estructuras de datos avanzadas
    lista = [1, 2, 3, "cuatro"]         #list
    tupla = (5, 6, 7, "ocho")           #tuple
    conjunto = {9, 10, "once", "doce"}  #set
    diccionario = {"clave1":"valor1","clave2": 20} #diccionarie

    print("Estructuras avanzadas:")
    print("Lista:",lista)
    print("Tupla:",tupla)
    print("Conjunto:",conjunto)
    print("Diccionario:",diccionario)

    # Otros tipos especiales
    nulo = None                     #NoneType
    rango = range(3)                #range (equivale a [0, ]) es decir, entrega cualquier numero pero sin contar el último y no almacena nada

    print("Tipos especiales:")
    print("Nulo:", nulo)
    print("Rango:", list(rango))    #Convertimos a lista

    # Ejemplo de iteración con el tipo range
    print("\nIterando sobre el rango:")

    #esta es la manera mas corta de recorrer un rango (for-each de python)
    for numero in rango:
     print(numero)