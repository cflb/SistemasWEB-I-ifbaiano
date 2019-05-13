from calculadora import soma, sub, div, mult

valor1 = int(input("Digite um valor: "))
valor2= int(input("digete outro valor: "))
operacao = input("digite a operacao + - / * ")

if operacao == "+":
    print(soma(valor1,valor2))
elif operacao == "-":
    print(sub(valor1,valor2))
elif operacao == "/":
    print(div(valor1, valor2))
elif operacao == "*":
    print(mult(valor1, valor2))
else:
    print("nao existe essa opcao")
