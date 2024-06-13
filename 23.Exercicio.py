#Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário.
#O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos. 
#Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.

def pergunta_numeros_primos():
    numero = int(input("Digite até que número quer que mostre os números primos :"))
    if numero > 0 :
            return numero
    else:
            print("Número menor que um")


           
def verifica_primo(numero):
    total_divisoes = 0
    numero_divisor = 2

    while numero_divisor <= numero:
        contador = 1
        divisor = 0
        while contador <= numero_divisor:
            total_divisoes += 1
            if numero_divisor % contador == 0:
                divisor += 1
            contador += 1
        
        if divisor == 2:  # Número primo tem exatamente dois divisores (1 e ele mesmo)
            print("Número primo:", numero_divisor)
        
        numero_divisor += 1

    print("Número total de divisões executadas:", total_divisoes) 
    
 

    




numero = pergunta_numeros_primos()
numero_divisor = verifica_primo(numero)

 