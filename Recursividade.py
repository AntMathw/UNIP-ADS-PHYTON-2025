def fatorial(n):
    if n < 0:
        return "Fatorial não definido para números negativos."
    elif n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

# Programa principal
numero = int(input("Digite um número inteiro para calcular o fatorial: "))
resultado = fatorial(numero)
print(f"O fatorial de {numero} é {resultado}")
