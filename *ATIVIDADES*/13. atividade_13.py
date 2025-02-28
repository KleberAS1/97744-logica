import os
os.system("clear")

#// Processamento.
valor_produto = float(input("Digite o valor do protudo (neste formato: 00.00): "))
print("""
============| PAGAMENTO |============
           
1. Á vista      
2. Parcelado    
      """)

forma_de_pagamento = int(input("Digite a forma de pagamento (1) (2): "))
os.system('cls' if os.name == 'nt' else 'clear')


match forma_de_pagamento:
    case 1:
        desconto = valor_produto * 0.10
        print("(1) Á vista")
        print("Você ganhou desconto (10%)")
        print(f"Valor do produto: {valor_produto}")
        print( f"*Valor final a pagar: {desconto}*")
        print()
        print()
    case 2:
        parcelas = int(input("Digite a quantidade de parcelas: "))
        parcelas = valor
        os.system('cls' if os.name == 'nt' else 'clear')
        print("(2) Parcelado")
        print(f"Valor do produto: {valor_produto}")
        print(f"Quantidades de parcelas: {parcelas}")
        print(f"Valor por parcela: {}")
    case _:
        print("Opção inválida")

#// Saída.






        

        

