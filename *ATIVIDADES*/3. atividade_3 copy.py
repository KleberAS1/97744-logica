#// Limpa terminal.
import os

os.system("clear")
#/////////////////

#// Processamento.
numero_um = int(input("Digite um número: "))
numero_dois = int(input("Digite outro número: "))

soma = numero_um + numero_dois
media = (numero_um + numero_dois) / 2
produto = numero_um * numero_dois

maior_numero = max(numero_um, numero_dois)
menor_numero = min(numero_um, numero_dois)
    


print()
print()
print(f"Média: {media}")
print(f"Soma: {int(soma)}")
print(f"Produto: {int(produto)}")

if numero_um == numero_dois:
    print(f"Maior número: Os números são iguais")
    print("Menor número: Os números são iguais")
else:    
    print(f"Maior número: {int(maior_numero)}")
    print(f"Menor número: {int(menor_numero)}")
print()    



