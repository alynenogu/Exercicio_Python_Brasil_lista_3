#Faça um programa que receba dois números inteiros e 
#gere os números inteiros que estão no intervalo compreendido por eles.


def pergunta_numero():

    numero = int(input("Digite o número: "))

    return numero

def maior_menor_numeros():
    contador = 0
    maior_numero = None
    menor_numero = None

    while contador <=2:
        numero = pergunta_numero()
        

        if maior_numero is None or numero > maior_numero:
            maior_numero = numero
        
        if menor_numero is None or numero < menor_numero:
            menor_numero = numero
        
        contador +=contador+1
    return maior_numero, menor_numero

def intervalo_dado(maior_numero, menor_numero):
    contador = menor_numero

    while contador <= maior_numero:
            print(contador)

            contador = contador + 1

        

maior_numero, menor_numero = maior_menor_numeros()


print(f"O maior número digitado foi: {maior_numero}")
print(f"O menor número digitado foi: {menor_numero}")
intervalo_dado(maior_numero, menor_numero)
