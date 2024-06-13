#Faça um programa que, dado um conjunto de N números, 
#determine o menor valor, o maior valor e a soma dos valores.

def pergunta_numero():
    numero = int(input("Digite o número do conjunto: - digite 000 para parar "))
    return numero

def lista_numero():
    contador = 0
    maior_numero = None
    menor_numero = None
    soma_valores = 0

    
    while True:
        numero = pergunta_numero()

        if numero == 0:
            break

        

        if maior_numero is None or numero > maior_numero:
            maior_numero = numero
        if menor_numero is None or numero < menor_numero:
            menor_numero = numero
        soma_valores += numero


       
     
 


    return maior_numero, menor_numero,soma_valores


maior_numero,menor_numero,soma_valores = lista_numero()

print(f"O maior número digitado foi: {maior_numero}")
print(f"O menor número digitado foi: {menor_numero}")
print(f"Soma: {soma_valores}")


