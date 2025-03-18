git add --exec-file calculadora.py
# Recebendo dados do usuário
num1 = float(input("insira um número:  "))
operacao = input("Escolha a operação (+, -, *, /, //): ")
num2 = float(input("insira o segundo número:  "))

if operacao == "+":
    print(num1, "+", num2, "=", num1 + num2)
elif operacao == "-":
    print(num1, "-", num2, "=", num1 - num2)
elif operacao == "*":
    print(num1, "*", num2, "=", num1 * num2)
elif operacao == "/":
    print (num1, "/", num2, "=", num1 / num2)
elif operacao == "//":
    print(num1, "//", num2, "=", num1 // num2)
else:
    print("Erro: Opção inválida!")
