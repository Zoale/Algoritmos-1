"""TP01-01 | MAYOR ENTRE TRES NÚMEROS
Desarrollar una función que reciba tres números positivos y devuelva el mayor de los tres, sólo si éste es único. En caso
de no existir un valor mayor único entonces devolver -1. No utilizar operadores lógicos (and, or, not). Desarrollar también
un programa para ingresar los tres valores, invocar a la función y mostrar el máximo hallado, o un mensaje informativo si
éste no existe."""
def ingresaNum(lista):
    num1 = int(input("Ingrese un numero"))
    while num1 < 0:
        num1 = int(input("Ingrese un numero"))
    lista.append(num1)
    num2 = int(input("Ingrese un numero2"))
    while num2 < 0:
        num2 = int(input("Ingrese un numero2"))
    lista.append(num2)
    num3 = int(input("Ingrese un numero3"))
    while num3 < 0:
        num3 = int(input("Ingrese un numero3"))
    lista.append(num3)
    return num1,num2,num3

def mayor(num1,num2,num3,lista):
    if num1 != num2:
        if num2 != num3:
            if num1 != num3:
                maximo = max(lista)
    else:
        maximo = -1
    return print(maximo)
    

def main():
    lista = []
    num1,num2,num3 = ingresaNum(lista)
    maximo = mayor(num1,num2,num3,lista)
    
main()
    