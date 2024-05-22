from math import factorial

l = int(input("Digite um número de 1 a 9: "))

num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))

numeros_encontrados = []

# Se l for maior que 9, definir l como 9
l = min(9, l)

for i in range(l):
    # Imprimindo espaços para centralizar
    print(" " * (l - i + 1), end=" ")
    
    for j in range(i + 1):
        # Calculando o coeficiente binomial e imprimindo
        coeficiente = factorial(i) // (factorial(j) * factorial(i - j))
        print(coeficiente, end=" ")

        if coeficiente == num1 or coeficiente == num2:
            numeros_encontrados.append(coeficiente)

    print("\n")

if num1 in numeros_encontrados:
    print(f"O número {num1} foi encontrado no triângulo de Pascal.")
if num2 in numeros_encontrados:
    print(f"O número {num2} foi encontrado no triângulo de Pascal.")