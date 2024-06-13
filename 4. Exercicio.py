#Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% 
#e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. 
#Faça um programa que calcule e escreva o número de anos necessários para que a população do país 
#A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

def verifica_cidade ():
    cidade_a = 80000
    cidade_b = 200000
    crescimento_a = 3
    crescimento_b = 1.5
    total_anos = 0
    
    while cidade_a < cidade_b:
       
       cidade_a += cidade_a * (crescimento_a/100)
       cidade_b += cidade_b * (crescimento_b/100)

       total_anos = total_anos + 1

    return total_anos
     


anos_necessarios = verifica_cidade()

print(f"Número de anos necessários para A ultrapassar ou igualar B: {anos_necessarios}")