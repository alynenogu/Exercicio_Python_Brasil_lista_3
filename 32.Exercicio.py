#Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. 
#Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:
#Fatorial de: 5
#5! =  5 . 4 . 3 . 2 . 1 = 120
#1 - Pergunta o número inteiro que deseja fazer fatorial
#2 - Depois calcula a fatorial pelo contador
#3 - Depois é necessário formatar a resposta

def pergunta_numero():
    numero = int(input("Qual é número que deseja fazer fatorial? "))
    if numero > 0:
        return numero
    else:
        print("Número negativo")
        return numero

def calcula_fatorial(numero):
    contador = numero
    resultado = 1
    fatorial_editada = ""

    while contador >0 :
        resultado *=contador
        
        fatorial_editada = f"{fatorial_editada}.{contador}"
        contador -= 1
    return resultado,fatorial_editada

numero = pergunta_numero()
resultado,fatorial_editada = calcula_fatorial(numero)

print(f"{numero}! = {fatorial_editada}")
