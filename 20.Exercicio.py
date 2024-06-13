#Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e 
#limitando o fatorial a números inteiros positivos e menores que 16.

def pergunta_numero():
    while True:
        numero = int(input("Qual número deseja ver o fatorial? (entre 1 e 15, ou 0 para sair): "))
        if 0 <= numero < 16:
            return numero
        else:
            print("Número não está entre 0 e 16. Tente novamente.")

def calcula_fatorial(numero):
    contador = 1
    fatorial = 1
    fatorial_editada = str(numero)
    
    while contador <= numero:
        fatorial *= contador
        if contador > 1:
            fatorial_editada = f"{fatorial_editada}.{contador}"
        contador += 1

    return numero, fatorial, fatorial_editada

while True:
    numero = pergunta_numero()
    if numero == 0:
        break
    
    numero, fatorial, resultado = calcula_fatorial(numero)
    print(f"{numero}! = {resultado} = {fatorial}")
