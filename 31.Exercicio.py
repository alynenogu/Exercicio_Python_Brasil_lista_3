#O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de 
# conveniências.
# Faça um programa que implemente uma caixa registradora rudimentar.
#  O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias.
# Um valor zero deve ser informado pelo operador para indicar o final da compra. 
# O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, 
# para então calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto
#  inicial, 
# para registrar a próxima compra. A saída deve ser conforme o exemplo abaixo:
# 1 - Pergunta o valor dos itens
# 2 - se for 0 deve indicar o final da compra
# 3 - Calcular o Total da Comprar
# 4 - Perguntar qual o valor que o cliente deu para pagar
# 5 - Calcular o Troco
# 6 - fazer a saída no seguinte modelo:
#Lojas Tabajara 
#Produto 1: R$ 2.20
#Produto 2: R$ 5.80
#Produto 3: R$ 0
#Total: R$ 9.00
#Dinheiro: R$ 20.00
#Troco: R$ 11.00
# 7 - Depois disso, perguntar a o valor do item novamente

def pergunta_valor():
    valor = float(input("Digite o preço do item: (Digite 0 para terminar a compra) "))
    if valor < 0:
        print("Valor Negativo")
        return pergunta_valor()
    else:
        return valor

def pergunta_valor_cliente():
    valor = float(input("Digite o valor dado pelo cliente:"))
    if valor < 0:
        print("Valor Negativo")
        return pergunta_valor()
    else:
        return valor

def lista_compra():
    soma_compra = 0
    valores = []
     
    while True:
        valor = pergunta_valor()
        if valor==0:
            break
        valores.append(valor)
        soma_compra +=valor
    return soma_compra,valores

def calcula_troco(valor_cliente,soma):

    troco =  valor_cliente - soma

    return troco





def realiza_compra ():
    soma_compra,valores = lista_compra()


    for i, valor in enumerate(valores, start=1):
        print(f"Produto {i} - {valor:.2f}")

    print(f"Soma da compra: {soma_compra:.2f}")
    valor_cliente = pergunta_valor_cliente()
    troco= calcula_troco(valor_cliente,soma_compra)
    print(f"Valor para dar ao cliente {troco:.2f}")

    var_saida = input("Deseja continuar? (S - sim)")
    if var_saida == "S":
        return realiza_compra()
    else:
        print("Ok, até a próxima")

realiza_compra ()