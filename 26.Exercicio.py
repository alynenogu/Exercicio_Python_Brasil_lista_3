#Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. 
#Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.
# 1 - Pergunta a quantidade de número total de eleitores
# 2 - Depois que tiver a quantidade, perguntar o voto
# 3 - se for A, conta 1, se for B, conta 1, se for C, conta 1
# 4 - Imprimir os votos

def pergunta_quantidade():
    quantidade = int(input("Digite a quantidade de eleitores "))
    if quantidade > 0:
        return quantidade
    else:
        print("Número menor que zero")
        return pergunta_quantidade()

def pergunta_voto(quantidade):
    contador = 0
    votos = []

    while contador < quantidade:
        voto = input("Digite seu voto para A, B ou C :").upper()
        if voto in ['A','B','C']:
            votos.append(voto)
            contador +=1
        else:
            print("Voto inválido, por favor vote em A, B ou C.")

    return votos

def calcula_votos(quantidade,votos):
    contador = 0
    quantidade_a =0
    quantidade_b =0
    quantidade_c =0

    while contador < quantidade:
        if voto[contador]=="A":
            quantidade_a +=1
        elif voto[contador]=="B":
            quantidade_b +=1
        elif voto[contador]=="C":
            quantidade_c +=1
        contador = contador + 1
    return quantidade_a,quantidade_b,quantidade_c



quantidade = pergunta_quantidade()
voto = pergunta_voto(quantidade)
print(f"Voto: {voto}")
quantidade_a,quantidade_b,quantidade_c = calcula_votos(quantidade,voto)
print(f"Quantidade A: {quantidade_a}")
print(f"Quantidade B: {quantidade_b}")
print(f"Quantidade C: {quantidade_c}")



