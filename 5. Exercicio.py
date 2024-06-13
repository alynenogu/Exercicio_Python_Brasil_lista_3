#Altere o programa anterior permitindo ao usuário informar 
#as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação


def pergunta_populacao_cidade():
    cidade = input("Diga a quantidade de pessoas na cidade: ")
    return cidade

def pergunta_crescimento_cidade():
    crescimento = input("Diga a o crescimento da população: ")
    return crescimento

def valida_dados():
    cidade_a = pergunta_populacao_cidade()
    while cidade_a.isnumeric()==False:
        print("Foi digitado um número não válido")
        cidade_a = pergunta_populacao_cidade()
    
    cresc_cidade_a = pergunta_crescimento_cidade()

    while cresc_cidade_a == float(cresc_cidade_a):
        print("Foi digitado um número não válido")
        cresc_cidade_a = pergunta_crescimento_cidade()
    
    cidade_b = pergunta_populacao_cidade()

    while cidade_b.isnumeric()==False:
        print("Foi digitado um número não válido")
        cidade_b = pergunta_populacao_cidade()
    
    cresc_cidade_b = pergunta_crescimento_cidade()

    while cresc_cidade_b == float(cresc_cidade_b):
        print("Foi digitado um número não válido")
        cresc_cidade_b = pergunta_crescimento_cidade()

    return int(cidade_a), int(cidade_b), float(cresc_cidade_a), float(cresc_cidade_b)

def verifica_cidade (cidade_a,cidade_b,cresc_cidade_a,cresc_cidade_b):
    total_anos = 0
    
    while cidade_a < cidade_b:
       
       cidade_a += cidade_a * (cresc_cidade_a/100)
       cidade_b += cidade_b * (cresc_cidade_b/100)

       total_anos = total_anos + 1

    return total_anos
     


cidade_a, cidade_b, cresc_cidade_a, cresc_cidade_b = valida_dados()


anos_necessarios = verifica_cidade(cidade_a,cidade_b,cresc_cidade_a,cresc_cidade_b)

print(f"Número de anos necessários para A ultrapassar ou igualar B: {anos_necessarios}")