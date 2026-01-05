try:
    num1 = int(input("Digite o primeiro numero: "))
    num2 = int(input("Digite o segundo numero: "))
    operacao = input("Digite a operação que deseja realizar (+, -, *, /): ")

    if operacao == '+':
        print(num1 + num2)
    elif operacao == '-':
        print(num1 - num2)
    elif operacao == '*':
        print(num1 * num2)
    elif operacao == '/':
        if num2 == 0:
            print("Erro: divisão por zero não permitida.")
        else:
            print(num1 / num2)
    else:
        print("Operação inválida.")
except ValueError:
    print("Erro: você deve digitar apenas números.")
