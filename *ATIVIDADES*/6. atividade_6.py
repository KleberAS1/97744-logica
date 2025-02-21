#// Limpa terminal.
import os 
os.system("clear")

#// Processamento.
numero_um = input("Digite um número: ")
numero_dois = input("Digite outro número: ")

if numero_um < numero_dois:
    maior_numero = numero_dois
    menor_numero = numero_um
else:
    maior_numero = numero_um
    menor_numero = numero_dois

#// Saída.
print()
print(f"Menor número {menor_numero}")
print(f"Maior número {maior_numero}")

