#// Limpa terminal.
import os
os.system("clear")
#// Processamento.
idade = int(input("Digite sua idade: "))
#// Saída.

if idade <16 or idade >65:
    print("Você não é obrigado a votar.")
elif idade == 16 or idade == 17:
    print("Seu voto é opcional")
else:
    print("Você é obrigado a votar.")


