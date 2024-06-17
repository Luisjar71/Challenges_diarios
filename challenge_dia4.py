# Ordenar lista: Escribe un programa que ordene una lista de números dada por el usuario en orden descendente

lista_num = input("Ingrese una lista de números separados por espacios: ")

lista_ordenada = []

for num in lista_num.split(","):
    lista_ordenada.append(int(num))

lista_ordenada.sort(reverse=True) 
print(lista_ordenada)
