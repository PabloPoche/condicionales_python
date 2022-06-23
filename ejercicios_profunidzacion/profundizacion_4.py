# Condicionales [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con texto
'''
Enunciado:
Realice un programa que solicite por consola 3 palabras cualesquiera
Luego el programa debe consultar al usuario como quiere ordenar las palabras
1 - Ordenar por orden alfabético (usando el operador ">")
2 - Ordenar por cantidad de letras (longitud de la palabra (len) y operador ">")

Si se ingresa "1" por consola se deben ordenar las 3 palabras por orden alfabético
e imprimir en pantalla de la mayor a la menor

Si se ingresa "2" por consola se deben ordenar las 3 palabras por cantidad de letras
e imprimir en pantalla de la mayor a la menor

IMPORTANTE: Para ordenar las palabras deben realizar condicionales compuestos o anidados,
no se busca utilizar bucles o algoritmos de ordenamiento ya que aún no hemos llegado a ese
contenido.
'''

print('Ejercicios de práctica con cadenas')
# Empezar aquí la resolución del ejercicio

# No se contemplara el caso de que las variables sean =, solo > o <.

palabra_1 = str(input("Ingrese la primer palabra:"))
palabra_2 = str(input("Ingrese la segunda palabra:"))
palabra_3 = str(input("Ingrese la tercer palabra:"))
orden = int(input("Ingrese 1 para odenarlas alfabeticamente o 2 por cantidad de letras: "))

if orden == 1:
    if palabra_1[0].lower() < palabra_2[0].lower() and palabra_1[0].lower() < palabra_3[0].lower():
        if palabra_2[0].lower() < palabra_3[0].lower():
            print(palabra_1, palabra_2, palabra_3)
        else:
            print(palabra_1, palabra_3, palabra_2)
    elif palabra_2[0].lower() < palabra_1[0].lower() and palabra_2[0].lower() < palabra_3[0].lower():
        if palabra_1[0].lower() < palabra_3[0].lower():
            print(palabra_2, palabra_1, palabra_3)
        else:
            print(palabra_2, palabra_3, palabra_1)
    elif palabra_3[0].lower() < palabra_1[0].lower() and palabra_3[0].lower() < palabra_2[0].lower():
        if palabra_1[0].lower() < palabra_2[0].lower():
            print(palabra_3, palabra_1, palabra_2)
        else:
            print(palabra_3, palabra_2, palabra_1)
        
if orden == 2:
    if (len(palabra_1) > len(palabra_2) and len(palabra_1) > len(palabra_3)):
        if len(palabra_2) > len(palabra_3):
            print(palabra_1, palabra_2, palabra_3)
        else:
            print(palabra_1, palabra_3, palabra_2)
    elif len(palabra_2) > len(palabra_1) and len(palabra_2) > len(palabra_3):
        if len(palabra_1) > len(palabra_3):
            print(palabra_2, palabra_1, palabra_3)
        else:
            print(palabra_2, palabra_3, palabra_1)
    elif len(palabra_3) > len(palabra_1) and len(palabra_3) > len(palabra_2):
        if len(palabra_1) > len(palabra_2):
            print(palabra_3, palabra_1, palabra_2)
        else:
            print(palabra_3, palabra_2, palabra_1)
        
