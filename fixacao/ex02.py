'''Questão 2 – Identificando tipos de dados
Crie variáveis contendo: 
•	Um texto
•	Um número inteiro
•	Um número decimal
•	Um valor booleano
Depois, utilize a função type() para exibir o tipo de cada variável.
Exemplo de saída:
<class 'str'>
<class 'int'>
<class 'float'>
<class 'bool'>
'''
name = "john"
age = 26
nasc = 2.1
boolean = True

print(type(name))
print(type(age))
print(type(nasc))
print(type(boolean))

"outra maneira de imprimir"

print(
    type(name),
    type(age),
    type(nasc),
    type(boolean),
)

"outra maneira de imprimir"
print(
    type(name), '\n',
    type(age), '\n',
    type(nasc), '\n',
    type(boolean),
)