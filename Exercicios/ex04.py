'''Questão 4 – Verificação de maioridade 

Crie uma variável chamada age.  

Utilize uma estrutura if...else para verificar a idade. 

Se for maior ou igual a 18, exiba: 

Maior de idade 

 

Caso contrário: 

Menor de idade '''

age = int(input("Qual sua idade?"))
# Ou apenas use age = 25
# Pois é o mais recomendado caso não peça o input

if age >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")