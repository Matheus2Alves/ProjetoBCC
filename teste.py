import re

user_password = input("Digite uma senha: \n")

def verificarSenha(user_password):

    if len(user_password) < 8:
        return False

    if not re.search(r'\d', user_password): 
       return False 

    if not re.search(r'[.,;:?!(){}<>^]', user_password):
        return False

    return True

if verificarSenha(user_password):
    print(f"'{user_password}' é uma senha forte")
else:
    print(f"'{user_password}' é uma senha fraca")