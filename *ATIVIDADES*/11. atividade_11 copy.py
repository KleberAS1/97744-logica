import os
os.system("clear")

#// Processamento.
print("""
            /------------\   
            | CALENDARIO |
       +----\------------/-----+
       |Segunda: 1   Sexta:   5|
       |Terça:   2   Sabado:  6|
       |Quarta:  3   Domingo: 7|
       |Quinta:  4             |
       +-----------------------+
      """)
             
dia_semana = int(input("Escreva o dia da semana em número (de 1 a 7): "))



match dia_semana:
    case 1 | 2 | 3 | 4 | 5 :
        dia_escrito = "Dia útil"
    case 6 | 7 :
        dia_escrito = "Final de semana."
    case _:
        dia_escrito = "Inválido"

#// Saída.
print()      
print(f" {dia_escrito}")
print()
print()

       