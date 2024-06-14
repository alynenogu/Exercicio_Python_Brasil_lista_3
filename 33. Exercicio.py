#O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia 
#as um conjunto indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas,
#bem como a média das temperaturas.
#1 - Perguntar qual temperatura
#2 - quando a situação 0 for inserida, mostra a menor e maior temperatura
#3 - também é necessário criar uma função para fazer a média

def pergunta_temperatura():
    temperatura = int(input("Digite a temperatura : digite 0 para sair: "))
    return temperatura

def lista_pergunta_temperatura():
    temperaturas = []
    soma_temperatura = 0
    Maior_temperatura = None
    Menor_temperatura = None
    quantidade_interacoes = 0
    while True:
        temperatura = pergunta_temperatura()
      
        if temperatura == 0:
            print("Até a próxima")
            break
        if Maior_temperatura is None or temperatura >Maior_temperatura  :
            Maior_temperatura = temperatura
        if Menor_temperatura is None or  temperatura < Menor_temperatura:
            Menor_temperatura = temperatura
        temperaturas.append(temperatura)
        soma_temperatura +=temperatura
        quantidade_interacoes +=1
    return soma_temperatura,Maior_temperatura,Menor_temperatura,quantidade_interacoes

def media_temperatura (soma,quantidade_interacoes):
    media = soma/quantidade_interacoes
    return media



soma_temperatura,Maior_temperatura,Menor_temperatura,quantidade_interacoes= lista_pergunta_temperatura()
print(f"Soma das temperaturas: {soma_temperatura}")
print(f"Maior das temperaturas: {Maior_temperatura}")
print(f"Menor das temperaturas: {Menor_temperatura}")
print(f"Quantidade de temperaturas: {quantidade_interacoes}")
media = media_temperatura(soma_temperatura,quantidade_interacoes)
print(f"Média de temperaturas: {media}")



