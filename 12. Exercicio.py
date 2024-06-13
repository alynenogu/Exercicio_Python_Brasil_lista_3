#Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10.
#O usuário deve informar de qual numero ele deseja ver a tabuada. 
#A saída deve ser conforme o exemplo abaixo:

def pergunta_numero ():

    numero = int(input("Digite o número da tabuada que deseja ver"))

    return numero

def define_tabuada(numero):
    contador = 1
    
    while contador <=10:
        multiplicacao = numero * contador
        print(f"{numero}*{contador}={multiplicacao}")

        contador = contador + 1

        

    


numero = pergunta_numero()

define_tabuada(numero)