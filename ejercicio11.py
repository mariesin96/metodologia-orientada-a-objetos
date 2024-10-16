def sumar(objeto1, objeto2):
    
    if isinstance(objeto1, (int, float)) and isinstance(objeto2, (int, float)):
        return objeto1 + objeto2
    
    elif isinstance(objeto1, list) and isinstance(objeto2, list):
        return objeto1 + objeto2
    
    elif isinstance(objeto1, str) and isinstance(objeto2, str):
        return objeto1 + objeto2
    else:
        raise TypeError("Los tipos de los objetos no son compatibles para sumar")


print(sumar(10, 20))           
print(sumar([1, 2], [3, 4]))   
print(sumar("Hola ", "Mundo"))