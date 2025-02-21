#// Limpa terminal.
import os
os.system("clear")

#// Processamento.
print("+-------------------------------+")
print("|            Maçãs              |")
print("+-------------------------------+")
print()
quantas_macas = int(input("Quantas maçãs você ira levar?: "))

if quantas_macas < 12:
    preco_maca = 1.30
else:
    preco_maca = 1.00

valor_total = quantas_macas * preco_maca

#// Saída.
print()
print("'--------| VALOR TOTAL |--------'")
print()
print(f"            R$ {valor_total:.2f}")
print()
print()
print()
print()



