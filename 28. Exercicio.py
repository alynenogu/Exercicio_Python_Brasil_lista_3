#Faça um programa que calcule o valor total investido por um colecionador em 
#sua coleção de CDs e o valor médio gasto em cada um deles. 
#O usuário deverá informar a quantidade de CDs e o valor para em cada um.
#1 - perguntar a quantidade de CDs
#2 - perguntar o valor de cada CD
#3 - somar o valor de cada CD
#4 - Calcular a média de valor (soma/quantidade)

def pergunta_quantidade():
    quantidade = int(input("Digite a quantidades de CDS :"))

    if quantidade > 0:
        return quantidade
    else:
        print("Número menor que zero")
        return pergunta_quantidade()

def pergunta_valor_cd():
    valor = float(input("Digite o valor do CD :"))

    if valor > 0:
        return valor
    else:
        print("Número menor que zero")
        return pergunta_valor_cd()

def verifica_valor_cd(quantidade):
    contador = 0
    valor = 0
    soma = 0

    while contador < quantidade:
        valor = pergunta_valor_cd()
        contador = contador + 1
        soma +=valor
    return valor,soma
def calcula_media(soma,quantidade):
    media = soma/quantidade

    return media

quantidade = pergunta_quantidade()
valor,soma = verifica_valor_cd(quantidade)
print(f"Valor da soma :{soma}")
resultado_media = calcula_media(soma,quantidade)
print(f"Valor da média :{resultado_media}")







