import os
os.system("clear")

#// Processamento.
print("""
            /------------\   
            | CALENDARIO |
            \------------/
 """)
dia_semana = int(input("Escreva o dia da semana em número (de 1 a 7): "))

match dia_semana:
    case 1:
        dia_escrito = "Segunda-feira"
        dia_utilidade = "Dia útil"
    case 2:
        dia_escrito = "Terça-feira"
        dia_utilidade = "Dia útil"
    case 3:
        dia_escrito = "Quarta-feira"
        dia_utilidade = "Dia útil"
    case 4:
        dia_escrito = "Quinta-feira"
        dia_utilidade = "Dia útil"
    case 5:
        dia_escrito = "Sexta-feira"
        dia_utilidade = "Dia útil"
    case 6:
        dia_escrito = "Sabado"
        dia_utilidade = "Final de semana"
    case 7:
        dia_escrito = "Domingo"
        dia_utilidade = "Final de semana"
    case _:
        dia_escrito = "Inválido"
        dia_utilidade = ""

#// Saída.
print()      
print(f" {dia_escrito}")
print(f" {dia_utilidade}")
       