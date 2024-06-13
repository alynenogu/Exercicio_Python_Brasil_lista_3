#Faça um programa que peça dois números, base e expoente,
#calcule e mostre o primeiro número elevado ao segundo número.
#Não utilize a função de potência da linguagem.

def pergunta_numero():
    base = int(input("Digite o valor da base: "))
    expoente = int(input("Digite o valor do expoente: "))

    return base, expoente

def calcula_valor(base, expoente):
    contador = 0
    resultado = 1

    while contador <expoente:

        resultado *= base 
        contador = contador + 1
    return resultado



base,expoente = pergunta_numero()

resultado = calcula_valor(base,expoente)

print(f"{base} elevado a {expoente} é {resultado}")