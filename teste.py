import re

#Recebe a senha do usuário
user_password = input("Digite uma senha para verificação: \n")
erros = []

#Verifica se a senha tem menos que 8 caracteres
if len(user_password) < 8:
    erros.append("A senha deve ter pelo menos 8 caracteres.")

#Verifica se a senha possuí número. O '\d' significa procurar por qualquer número
if not re.search(r'\d', user_password):
    erros.append("A senha deve conter pelo menos um numero.")

#Verifica se a senha possuí um caractere especial
if not re.search(r'[., ;: ` ~! @#$%^&*()_+=|{}[\]-]', user_password):
    erros.append("A senha deve conter pelo menos um caractere especial (ex: !, @, #, $).")

#Verifica se a senha possui letra maiúscula
if not re.search(r'[a-z]', user_password) or not re.search(r'[A-Z]', user_password):
    erros.append("A senha deve conter letras maiúsculas e minusculas.")

#Expõe para o usuário o resultado do processamento
if not erros:
    print(f"'{user_password}' e uma senha forte!")
else:
    print(f"'{user_password}' é uma senha fraca.")
    print("\nMotivos e Sugestões:")
    for erro in erros:
        print(f". {erro}")

