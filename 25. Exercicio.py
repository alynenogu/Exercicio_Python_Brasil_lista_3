#Faça um programa que peça para n pessoas a sua idade, 
#ao final o programa devera verificar se a média de idade da turma 
#varia entre 0 e 25,26 e 60 e maior que 60;
#e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada

# 1 - Perguntar a quantidade de pessoas
# 2 - Perguntar a idade das pessoas
# 3 - Se a pessoa tem entre 0 ou 25 anos, conta 1
# 4 - Se a pessoa tem 26 e 60, conta 1
# 5 - Se a pessoa tem maior que 60, conta 1
# 6 - Se tiver mais jovens, turma jovem, se tiver mais adulta, turma adulta, se tiver idosa, turma idosa

def pergunta_quantidade():
    quantidade = int(input("Digite a quantidade de pessoas da turma :"))
    if quantidade > 0:
        return quantidade
    else:
        print("Número menor que um")
        return pergunta_quantidade()
    
def pergunta_idade(quantidade):
    contador = 0
    idades = []
    while contador < quantidade :
        idade = int(input("Digite a sua idade :"))
        idades.append(idade)
        contador +=1
    return idades

def calcula_media(idade, quantidade):
    
    media =  sum(idade)/quantidade

    return media

def verifica_faixa(media):

        if 0 > media or media  < 25 :
            return print("Turma Jovem")
        if 25> media or media <= 60 :
            return print("Turma Adulta")
        if media > 60 :
            return print("Turma idosa")
        else:
            return print("Verificar if")
     

     
    

quantidade = pergunta_quantidade()
idade = pergunta_idade(quantidade)
media = calcula_media(idade,quantidade)


print(f"Idade da pessoa: {idade}")
print(f"Média de idade: {media}")
verifica_faixa(media)
