# Limpa terminal
import os
os.system("clear")

# Dados cadastrados
usuario_cadastrado = "Juninho"
senha_cadastrada = "12345678"

# Entrada do usuário
usuario = input("Digite seu usuario: ")
senha = input("Digite sua senha: ")

# Validação do login
if senha == senha_cadastrada and usuario == usuario_cadastrado:
    print("Bem-vindo de volta :)")
else:
    print("Login ou senha inválidos. Acesso não liberado")
