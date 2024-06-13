#Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.

def imprimir_valores():

    
    contador = 0
    numero = 1

    while contador <=50:
        if numero % 2 !=0:
            print (numero, end =' ')
        contador = contador + 1
        numero = numero + 1


numero = imprimir_valores()


print(numero)
