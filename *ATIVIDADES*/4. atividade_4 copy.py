#// Limpa terminal.
import os

os.system("clear")
#/////////////////

#// Processemanto.
usuario_cadastrado = "Juninho"
senha_cadastrada = "12345678"

usuario = str(input("Digite seu usuario: "))
senha = int(input("Digite sua senha: "))

if senha == senha_cadastrada and usuario == usuario_cadastrado:
    print("Bem vindo de volta :)")
else:
    print("Login ou senha invalidas. Acesso não liberado")
print()    


#// Saída.



    
