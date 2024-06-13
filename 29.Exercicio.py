#O Sr. Manoel Joaquim possui uma grande loja de artigos de R$ 1,99, com cerca de 10 caixas.
#Para agilizar o cálculo de quanto cada cliente deve pagar ele desenvolveu um tabela que contém o 
#número de itens que o cliente comprou e ao lado o valor da conta.
#Desta forma a atendente do caixa precisa apenas contar quantos itens o cliente está levando e olhar na 
#tabela de preços. Você foi contratado para desenvolver o programa que monta esta tabela de preços, 
#que conterá os preços de 1 até 50 produtos, 
#conforme o exemplo abaixo:
#Lojas Quase Dois - Tabela de preços
#1 - R$ 1.99
#2 - R$ 3.98
#...
#50 - R$ 99.50
# 1 - Perguntar o preço
# 2 - Como é de 1 até 50, ir multiplicando  o valor até o 50
def perguntar_qtd_itens():
    qtd_itens = int(input("Quantidade de itens da lista? "))
    if qtd_itens > 0:
        return qtd_itens
    else:
        print("quantidade de itens menor que zero ")    
        return perguntar_qtd_itens()

def perguntar_preco():
    preco = float(input("Qual o preço do item? "))
    if preco > 0:
        return preco
    else:
        print("valor menor que zero ")    
        return perguntar_preco()

def calcula_preco(quantidade_itens,preco):
    contador = 1
    resultado = 0

    while contador < quantidade_itens:
        resultado = preco * contador
        print (f"{contador} - {resultado}")
        contador +=1

        

qtd_itens = perguntar_qtd_itens()
 
preco = perguntar_preco()  
calcula_preco(qtd_itens,preco)      
