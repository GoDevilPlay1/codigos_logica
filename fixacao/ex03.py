'''Questão 3 – Lista de frutas 

Crie uma lista contendo pelo menos 5 frutas. 

Depois: 

Exiba a lista completa. 

Exiba apenas a primeira fruta. 

Exiba apenas a última fruta. 

Adicione algumas frutas e exiba a última, independentemente da quantidade. 

 '''

frutas = ["banana", "pêra", "uva", "morango", "maçã"]

print(frutas)

print(len(frutas))

print()

print(frutas[0])

print(frutas[4])
# ou, independente da quantidade de itens na coleção
print(frutas[-1]) # dessaa forma

print()
frutas.insert(5, "mamão")

print(len(frutas))

print(frutas[5])
