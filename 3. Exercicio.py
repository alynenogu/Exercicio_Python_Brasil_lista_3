#Faça um programa que leia e valide as seguintes informações:
#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Sexo: 'f' ou 'm';
#Estado Civil: 's', 'c', 'v', 'd';

def pergunta_nome():
    nome = input("Qual é o nome: ")

    return nome

def pergunta_idade():
    idade = int(input("Qual é a idade: "))

    return idade

def pergunta_salario():
    salario = float(input("Qual é o salário: "))

    return salario

def pergunta_genero():
    genero = input("Qual é o gênero: ")

    return genero

def pergunta_estado_civil():
    estado_civil = input("Qual é o seu estado civil: ")

    return estado_civil

def valida_dados():

    nome = pergunta_nome()
    while len(nome)<3:
        print("Nome inválido! Tem que ser maior que 3 caracteres")
        nome = pergunta_nome()

    idade = pergunta_idade()
    while idade < 0 or idade > 150:
        print("Idade inválida, tente novamente")
        idade = pergunta_idade()

    salario = pergunta_salario()
    while salario < 0:
        print("Salário errado, tente novamente")
        salario = pergunta_salario()

    genero = pergunta_genero()
    while genero != "f" and genero != "F" and genero != "m" and genero != "M" :
        print("gênero errado, por gentileza corrigir")
        genero = pergunta_genero()
    
    estado_civil = pergunta_estado_civil()
    while estado_civil != "s" and estado_civil != "c" and estado_civil != "v" and estado_civil != "d" :
        print("estado civil errado, por gentileza corrigir")
        estado_civil = pergunta_estado_civil()



valida_dados()