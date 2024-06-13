#Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.#

#Faça um programa que, dado um conjunto de N números, 
#determine o menor valor, o maior valor e a soma dos valores.

def pergunta_numero():
    numero = int(input("Digite o número do conjunto: - digite 0 para parar e números entre 0 e 1000 "))
    return numero

def lista_numero():
    contador = 0
    maior_numero = None
    menor_numero = None
    soma_valores = 0

    
    while True:
        numero = pergunta_numero()

        if numero == -1:
            break
        if 0 < numero and  numero > 1000:
            print("Número não está entre 0 ou 1000")
            continue

        

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


