from math import factorial

# Função para calcular a combinação C(m, p)
def combinacao(m, p):
    return factorial(m) // (factorial(p) * factorial(m - p))

# Solicitar ao usuário os valores de m, p e l
m = int(input("Digite o valor de m: "))
p = int(input("Digite o valor de p: "))
l = int(input("Digite um número de 1 a 9, o numero selecionado vai ser usado na criado da piramide de pascal: "))

# Verificar se p está dentro do intervalo válido
if p > m or p < 0:
    print("Valor inválido para p. Ele deve estar entre 0 e m (inclusive).")
else:
    # Calcular o valor da combinação C(m, p)
    resultado_combinacao = combinacao(m, p)
    print(f"C({m}, {p}) = {resultado_combinacao}")

    numeros_encontrados = []

    # Se l for maior que 9, definir l como 9
    l = min(9, l)

    # Construir o triângulo de Pascal e procurar o resultado
    for i in range(l):
        # Imprimindo espaços para centralizar
        print(" " * (l - i + 1), end=" ")
        
        for j in range(i + 1):
            # Calculando o coeficiente binomial e imprimindo
            coeficiente = factorial(i) // (factorial(j) * factorial(i - j))
            print(coeficiente, end=" ")

            if coeficiente == resultado_combinacao:
                numeros_encontrados.append(coeficiente)

        print("\n")

    if resultado_combinacao in numeros_encontrados:
        print(f"O resultado da combinação {resultado_combinacao} foi encontrado no triângulo de Pascal.")
    else:
        print(f"O resultado da combinação {resultado_combinacao} não foi encontrado no triângulo de Pascal.")
