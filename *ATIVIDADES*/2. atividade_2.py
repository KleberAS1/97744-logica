#// Limpa terminal.
import os 
os.system("clear")
#//////////////////

#// Processamento.
nota_um = float(input("Digite sua primeira nota: "))
nota_dois = float(input("Digite sua segunda nota: "))
nota_tres = float(input("Agora digite sua terceira nota: "))

soma = (nota_um + nota_dois + nota_tres) // 3

#// Saída.
print()
print("¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨")
print(f"Média: {soma}")
print()
if soma < 7:
    print("Aluno Reprovado")
else:
    print("Aluno aprovado")
    print()
    print("¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨")
    print()