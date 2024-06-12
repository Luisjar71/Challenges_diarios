def invertir_caracteres(cadena_de_caracteres):
    if len(cadena_de_caracteres) == 0:
        return ""
    
    else:
        return cadena_de_caracteres[-1] + invertir_caracteres(cadena_de_caracteres[:-1])
    
resultado = invertir_caracteres("Manchester United")
print(resultado)