#Faça um programa que leia 5 números e informe a soma e a média dos números.


def pergunta_numero():
    numero = int(input("Digite o número:"))

    return numero

def soma_numero():

    contador = 0 

    soma = 0
    media = 0

    while contador <=5:

        numero = pergunta_numero()

        soma += numero
        media = soma/5

        contador = contador+1

    return soma,media




soma,media = soma_numero()

print(f"A soma foi: {soma}")

print(f"A média foi: {media}")

