numero = int(input("Ingrese un número para multiplicar: "))

for i in range(1, 10):
    resultado = (numero * i)
    i += 1
    print(f" -> {resultado}")
