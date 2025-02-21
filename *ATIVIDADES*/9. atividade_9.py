#// Limpa terminal.
import os
os.system("clear")

#// Processamento.
print("+-------------------+")
print("|    CALCULADORA    |")
print("|     ¦+ - * /¦     |")
print("+-------------------+")


numero_um = int(input("Digite um número: "))
numero_dois = int(input("Digite outro número: "))
operacao = input("Digite a operação da conta: ")
print()

match operacao:
    case "+":
        resultado = numero_um + numero_dois
    case "-":
        resultado = numero_um - numero_dois
    case "*":
        resultado = numero_um * numero_dois
    case "/":
        resultado = numero_um / numero_dois
    case _:
        print("Invalido.")

#// Saída.
print("---------------+")
print(f"Numero um: {numero_um}   | ")
print(f"Operação:  {operacao}   | ")
print(f"Numero dois: {numero_dois} | ")
print("---------------+")
print(f"Resultado:   {resultado}")
print("================")
print()
print()


