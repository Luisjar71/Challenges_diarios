#  Crear un Diccionario: Escribe un programa que cree un diccionario a partir de dos listas dadas: una de claves y otra de valores.

diccionario = {}

claves = [1, 2, 3, 4, 5]
valores = ["león", "tigre", "lobo", "puma", "gato"]

for i in range(len(claves)):
    diccionario[claves[i]] = valores[i]

print(diccionario)

