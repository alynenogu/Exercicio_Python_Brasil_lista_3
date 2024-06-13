#Faça um programa que calcule o número médio de alunos por turma. 
#Para isto, peça a quantidade de turmas e a 
#quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.
# 1 - Pergunta número de turmas
# 2 - Pergunta a quantidade de alunos (com validação que a turma não pode ter mais de 40 alunos)
# 3 - calcular a média da tuma (quantidade de alunos divido por quantidade de turmas)

def pergunta_quantidade():
    quantidade = int(input("Qual a quantidade de turmas :"))

    if quantidade > 0:
        return quantidade
    else:
        print("Número menor que zero")
        return pergunta_quantidade()
    

def pergunta_quantidade_alunos():
    quantidade_alunos = int(input("Qual a quantidade de alunos: "))

    if quantidade_alunos <= 40:
        return quantidade_alunos
    else:
        print("Passou de 40")
        return pergunta_quantidade_alunos()
    
def verifica_alunos(quantidade):
    contador = 0
    quantidade_alunos = 0

    while contador <quantidade:
        quantidade_alunos = pergunta_quantidade_alunos()
        contador = contador + 1
    
    return quantidade_alunos

def calcula_media (quantidade, quantidade_alunos):
    media = quantidade_alunos/quantidade

    return media

quantidade = pergunta_quantidade()
quantidade_alunos = verifica_alunos(quantidade)
media_final = calcula_media(quantidade,quantidade_alunos)

print(f"A média de alunos é: {media_final}")

