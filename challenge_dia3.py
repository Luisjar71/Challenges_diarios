# Contar Vocales: Escribe un programa que cuente el número de vocales en una cadena dada.

palabra = input("Ingrese una palabra: ")


contador = 0
for i in palabra:
    if i in ["a", "e", "i", "o", "u"]:
        contador += 1

print(contador)



