#Faça um programa que calcule o fatorial de um número inteiro 
#fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

def pergunta_numero():

    numero = int(input("Qual número deseja ver o fatorial? "))
    return numero

def calcula_fatorial(numero):
    contador = 1
    fatorial_editada = numero
    fatorial =1
    
    while contador <= numero:
        fatorial = fatorial * contador
        fatorial_editada = f"{fatorial_editada}.{contador}"
   
        contador = contador + 1

    return   fatorial, fatorial_editada

numero = pergunta_numero()
fatorial, resultado = calcula_fatorial(numero)

print(f"{numero}! = {resultado} = {fatorial} ")

