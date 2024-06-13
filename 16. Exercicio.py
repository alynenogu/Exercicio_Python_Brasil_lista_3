#A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... 
#Faça um programa que gere a série até que o valor seja maior que 500.
 
def sequencia_fibonacci():
    a = 1
    b = 1
    contador = 2
    fibonacci = [a, b]  # Começando com os dois primeiros termos da série
    
    while True:
        t = a + b
        if t > 500:
            break
        
        fibonacci.append(t)
        a = b
        b = t
        contador += 1
    
    return fibonacci

 
resultado = sequencia_fibonacci()

print(f"A série de Fibonacci até o : {resultado}")