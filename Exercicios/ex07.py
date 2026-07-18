'''Questão 7 – Acesso ao sistema (operador AND) 

Crie as variáveis: 

usuario = "admin" 

senha = "1234" 

Utilize o operador and para verificar se: 

usuário é "admin" 

senha é "1234" 

Se ambas as condições forem verdadeiras: 

Acesso permitido. 

  

Caso contrário: 

Acesso negado. '''

usuario = "admin"
senha = "1234"

#         True                 True
if usuario == "admin" and senha == "1234":
    print("Acesso Liberado")
else:
    print("Acesso Negado")