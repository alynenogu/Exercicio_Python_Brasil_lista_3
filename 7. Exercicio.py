#Faça um programa que leia 5 números e informe o maior número.

def pergunta_numero():

    numero = int(input("Digite o número: "))

    return numero

def verifica_numero():
    contador = 0
    maior_numero = None

    while contador <=5:
        numero = pergunta_numero()

        if maior_numero is None or numero > maior_numero:
            maior_numero = numero




        contador = contador + 1

    return maior_numero





maior_numero = verifica_numero()

print(f"O maior número digitado foi: {maior_numero}")