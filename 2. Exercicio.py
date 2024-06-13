#Faça um programa que leia um nome de usuário e a sua senha e 
#não aceite a senha igual ao nome do usuário, 
#mostrando uma mensagem de erro e voltando a pedir as informações.


def pergunta_nome():
    
    nome = input("Digite seu nome: ")

    return nome

def pergunta_senha():

    senha = input("Digite sua senha: ")
    return senha

def validar_senha(nome,senha):

    while nome ==senha:
        print("nome igual a senha, continue tentando")
        nome = pergunta_nome()
        senha = pergunta_senha()


nome = pergunta_nome()
senha = pergunta_senha()

validar_senha(nome, senha)

