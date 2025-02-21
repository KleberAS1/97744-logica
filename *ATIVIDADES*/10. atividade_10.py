#// Limpa terminal.
import os
os.system("clear")

#// Processamento.
print("""
======================= MENU ========================
Código  \t\tPrato   \t\tValor 
1    \t\t\tPicanha     \t\t25,00    
2     \t\t\tLasanha     \t\t20,00    
3     \t\t\tEstrogonoff     \t18,00    
4     \t\t\tBife acebolado     \t15,00    
5     \t\t\tPão com ovo      \t05,00
""")

opcao = int(input("Digite a opção desejada: "))

#//

match opcao:
    case 1:
        prato = "Picanha"
        valor = "25"
    case 2:
        prato = "Lasanha"
        valor = "20"
    case 3:
        prato = "Estrogonoff"
        valor = "18"
    case 4:
        prato = "Bife acebolado"
        valor = "15"
    case 5:
        prato = "Pao com ovo"
        valor = "5"
    case _:
        prato = "Inválido"    
        valor = 0

#// Saída.
print()
print(f"Prato: {prato}")
print(f"Valor: {valor}")
print()
print()