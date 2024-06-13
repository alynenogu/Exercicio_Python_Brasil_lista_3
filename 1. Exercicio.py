#Faça um programa que peça uma nota, entre zero e dez.
# Mostre uma mensagem caso o valor seja inválido 
#e continue pedindo até que o usuário informe um valor válido.

def perguntanota():
    

    return  input("Digite a nota entre zero e dez: ")

def valida_numero(numero):

    while numero.isdigit()==False:
       
        print("Foi digitado um número não válido")
        numero = perguntanota()
    
    while  int(numero) > 10:
        print("Foi digitado um valor maior que 10")
        numero = perguntanota()

  

nota1= perguntanota()
valida_numero(nota1)
 

