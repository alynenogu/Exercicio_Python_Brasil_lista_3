# A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... 
# Faça um programa capaz de gerar a série até o n−ésimo termo.

def pergunta_numero():
    numero = int(input("Digite o termo n para a série de Fibonacci: "))
    return numero

def sequencia_fibonacci(numero):
    a = 1
    b = 1
    contador = 2
    fibonacci = [a, b]  # Começando com os dois primeiros termos da série
    
    while contador < numero:
        t = a + b
        fibonacci.append(t)
        a = b
        b = t
        contador += 1
    
    return fibonacci

numero = pergunta_numero()
resultado = sequencia_fibonacci(numero)

print(f"A série de Fibonacci até o {numero}º termo é: {resultado}")
