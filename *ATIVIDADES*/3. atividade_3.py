#// Limpa terminal.
import os

os.system("clear")
#/////////////////

#// Processamento.
numero_um = float(input("Digite um numero: "))
numero_dois = float(input("Digite outro número: "))

soma = numero_um + numero_dois
media = (numero_um + numero_dois) / 2
produto = numero_um * numero_dois

if numero_um < numero_dois:
    maior_numero = numero_dois
    menor_numero = numero_um
else:
    maior_numero = numero_um
    menor_numero = numero_dois



print()
print(f"Média: {media}")
print(f"Soma: {int(soma)}")
print(f"Produto: {int(produto)}")

if numero_um == numero_dois:
    print(f"Maior número: Os números são iguais")
    print("Menor número: Os números são iguais")
    print()
else:    
    print(f"Maior numero: {int(maior_numero)}")
    print(f"Menor numero: {int(menor_numero)}")
    print()


