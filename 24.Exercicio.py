#Faça um programa que calcule o mostre a média aritmética de N notas.
# 1- Pedir a quantidade de notas que vão ser mostradas
# 2 - Pedir as notas até um determinada quantidade
# 3 - Fazer média aritmetica

def pergunta_quantidade():
    numero = int(input("Digite a quantidade de notas que serão divulgadas: "))
    if numero > 0:
        return numero
    else:
        print("Número menor que um")
        return pergunta_quantidade()

def digite_notas(quantidade):
    contador = 0
    soma = 0

    while contador < quantidade:
        nota = int(input("Digite a nota: "))
        if nota >= 0:
            soma += nota
            contador += 1
        else:
            print("Digite uma nota maior ou igual a 0")

    return soma

def calcula_media(soma,quantidade):
    
    media = soma/quantidade

    return media








quantidade = pergunta_quantidade()
total_soma = digite_notas(quantidade)
print(f"A soma das notas é: {total_soma}")
media = calcula_media(total_soma,quantidade)
print(f"A média é: {media}")

    
                 

               
            



