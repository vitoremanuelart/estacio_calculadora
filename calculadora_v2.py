saida = ""

def adicao(num1, num2):
    soma = float(num1) + float(num2)
    return soma

def subtracao(num1, num2):
    subt = float(num1) - float(num2)
    return subt

def multiplicacao(num1, num2):
    mult = float(num1) * float(num2)
    return mult

def divisao(num1, num2):
    divi = float(num1) / float(num2)
    return divi

def calculadora(num1, num2, operacao):

    if str(operacao) == "adicao" or str(operacao) == "+":
        resultado = adicao(num1, num2)
        return resultado
    elif str(operacao) == "subtracao" or str(operacao) == "-":
        resultado = subtracao(num1, num2)
        return resultado
    elif str(operacao) == "multiplicacao" or str(operacao) == "*":
        resultado = multiplicacao(num1, num2) 
        return resultado
    elif str(operacao) == "divisao" or str(operacao) == "/":
        resultado = divisao(num1, num2)
        return resultado
    else:
        print("A operação solicitada é inválida.")
        resultado = ""
        return resultado

print("Seja bem-vindo(a) à Calculadora!")

while saida.lower() != "n":

    num1 = input("Insira um número: ")
    num2 = input("Insira outro número: ")
    oper = input("Insira uma operação matemática (+ - * /): ")
    resultado_calc = calculadora(num1, num2, oper)

    print(f"Resultado da operação: {resultado_calc}")

    saida = input("Deseja continuar? (S/N)\n")

print("Entendido, fechando a calculadora. Estarei aqui para ajudar sempre que precisar!")
