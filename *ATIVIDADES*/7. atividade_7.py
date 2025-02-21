#// Limpa terminal.
import os 
os.system("clear")

#// Processamento.
numero_um = int(input("Digite um número: "))
numero_dois = int(input("Digite outro número: "))
numero_tres = int(input("Agora um último número: "))

maior_numero = max(numero_um, numero_dois, numero_tres)
menor_numero = min(numero_um, numero_dois, numero_tres)

#// Saída.
print()
print(f"Números: {numero_um, numero_dois, numero_tres}")
print(f"Menor número: {menor_numero}")
print(f"Maior número: {maior_numero}")


