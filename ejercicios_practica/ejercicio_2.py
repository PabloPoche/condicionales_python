# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Comparadores
# Ingrese dos palabras cualesquiera y realice las sigueintes
# comparaciones entre ellas
texto_1 = str(input('Ingrese la primera palabra:'))
texto_2 = str(input('Ingrese la segunda palabra:'))

# Compare cual de las dos palabras es mayor (alfabéticamente)
# Imprima en pantalla según corresponda
if texto_1 == texto_2:
    print("Los dos textos son iguales")
elif texto_1 > texto_2:
    print("El primer texto es mayor")
else: 
    print("El segundo texto es mayor")

# Compare cual de las dos palabras tiene mayor
# cantidad de letras
# Imprima en pantalla según corresponda
if len(texto_1) == len(texto_2):
    print("Los dos textos tiene igual cantidad de letras")
elif len(texto_1) > len(texto_2):
    print("El primer texto tiene mayor cantidad de letras")
else: 
    print("El segundo texto tiene mayor cantidad de letras")

# Verifique si la primera letra de la primera palabra
# es mayor a la primera letra de la segunda palabra
# Imprima en pantalla según corresponda
if texto_1[0] == texto_2[0]:
    print("Los dos textos tiene la primer letra igual")
elif texto_1[0] == texto_2[0]:
    print("La primera letra del primer texto es mayor a la primer letra del segundo texto")
else: 
    print("La primera letra del segundo texto es mayor a la primer letra del primer texto")

copia_texto_1 = texto_1  # Copia de la variable texto_1

# Verifique que copia_texto_1 es igual a texto_1
# Imprima en pantalla según corresponda
if copia_texto_1 == texto_1:
    print(copia_texto_1, "es igual a", texto_1)

# Verifique que copia_texto_1 es distinta a texto_2
# Imprima en pantalla según corresponda
if copia_texto_1 != texto_2:
    print(copia_texto_1, "es distinto a", texto_2)
