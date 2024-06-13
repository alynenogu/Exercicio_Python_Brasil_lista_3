#Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. 
#Um número primo é aquele que é divisível somente por ele mesmo e por 1.


def pergunta_numero():
    numero = int(input("Digite o número que deseja verificar se é primo :"))
    if numero > 0 :
            return numero
    else:
            print("Número menor que um")


def verifica_primo(numero):
    contador = 1
    divisor = 0

    while contador < numero+1:
        if numero % contador == 0:
            print("Múltiplo de ", contador)
            divisor += 1
        contador = contador + 1

    if divisor == 2:
        print("é  número primo")
    else:
        print("não é número primo")

numero = pergunta_numero()
verifica_primo(numero)