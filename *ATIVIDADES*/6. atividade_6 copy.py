#// Limpa terminal.
import os 
os.system("clear")

#// Processamento.
numero_um = input("Digite um número: ")
numero_dois = input("Digite outro número: ")

maior_numero = max(numero_um, numero_dois)
menor_numero = min(numero_um, numero_dois)
#// Saída.
print()
print(f"Menor número {menor_numero}")
print(f"Maior número {maior_numero}")

