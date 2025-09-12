# Definindo as funções para as operações
def adicionar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    # Usamos um try-except para evitar erro de divisão por zero
    try:
        return x / y
    except ZeroDivisionError:
        return "Erro! Divisão por zero não é permitida."

# Apresentação da calculadora
print("Selecione a operação desejada:")
print("1. Adicionar")
print("2. Subtrair")
print("3. Multiplicar")
print("4. Dividir")

# Loop principal da calculadora
while True:
    # Recebe a escolha do usuário
    escolha = input("Digite sua escolha (1/2/3/4): ")

    # Verifica se a escolha é válida
    if escolha in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")
            continue

        if escolha == '1':
            print(f"Resultado: {adicionar(num1, num2)}")

        elif escolha == '2':
            print(f"Resultado: {subtrair(num1, num2)}")

        elif escolha == '3':
            print(f"Resultado: {multiplicar(num1, num2)}")

        elif escolha == '4':
            print(f"Resultado: {dividir(num1, num2)}")
        
        # Pergunta ao usuário se ele quer fazer outro cálculo
        proximo_calculo = input("Quer fazer outro cálculo? (sim/não): ")
        if proximo_calculo.lower() != 'sim':
            break

    else:
        print("Escolha inválida.")