#Altere o programa de cálculo dos números primos, 
#informando, caso o número não seja primo, por quais número ele é divisível.

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
            if divisor == 2:
                print("é  número primo")
            else:
                print("Múltiplo de ", contador)
                print("não é número primo")
            divisor += 1
        contador = contador + 1

    

numero = pergunta_numero()
verifica_primo(numero)