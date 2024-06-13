#O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar a metodologia da tabelinha, 
# #que já é um sucesso na sua loja de 1,99. 
# #Você foi contratado para desenvolver o programa que monta a tabela de preços de pães, 
# de 1 até 50 pães, 
#a partir do preço do pão informado pelo usuário, conforme o exemplo abaixo:

def perguntar_qtd_paes():
    qtd_itens = int(input("Quantidade de pães? "))
    if qtd_itens > 0:
        return qtd_itens
    else:
        print("quantidade de pães menor que zero ")    
        return perguntar_qtd_paes()

def perguntar_preco():
    preco = float(input("Qual o preço do pão? "))
    if preco > 0:
        return preco
    else:
        print("valor menor que zero ")    
        return perguntar_preco()

def calcula_preco(quantidade_preco,preco):
    contador = 1
    resultado = 0

    while contador < quantidade_preco:
        resultado = preco * contador
        print (f"{contador} - {resultado}")
        contador +=1

        

qtd_paes = perguntar_qtd_paes()
 
preco = perguntar_preco()  
print(f"Preço do pão: {preco}")
print("Panificadora Pão de Ontem - Tabela de preços")
calcula_preco(qtd_paes,preco)      
