#Faça um programa que peça 10 números inteiros, 
#calcule e mostre a quantidade de números pares e a quantidade de números impares.

def pergunta_numero():
    numero = int(input("Digite um número inteiro: "))
    return numero

def verifica_pares_impares():
    contador = 0 
    quantidade_impares = 0
    quantidade_pares = 0

    while contador < 10:  
        numero = pergunta_numero()

        if numero % 2 == 0:
            quantidade_pares += 1  
        else:
            quantidade_impares += 1  

        contador += 1  
    return quantidade_pares, quantidade_impares

pares, impares = verifica_pares_impares()

print(f"{pares} - quantidade de números pares")
print(f"{impares} - quantidade de números ímpares")
