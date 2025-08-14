import re

user_password = input("Digite uma senha para verificação: \n")
erros = []

if len(user_password) < 8:
    erros.append("A senha deve ter pelo menos 8 caracteres.")

if not re.search(r'\d', user_password):
    erros.append("A senha deve conter pelo menos um numero.")

if not re.search(r'[., ;: ` ~! @#$%^&*()_+=|{}[\]-]', user_password):
    erros.append("A senha deve conter pelo menos um caractere especial (ex: !, @, #, $).")

if not re.search(r'[a-z]', user_password) or not re.search(r'[A-Z]', user_password):
    erros.append("A senha deve conter letras maiúsculas e minusculas.")

if not erros:
    print(f"'{user_password}' e uma senha forte!")
else:
    print(f"'{user_password}' é uma senha fraca.")
    print("\nMotivos e Sugestões:")
    for erro in erros:
        print(f". {erro}")

        