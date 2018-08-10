#Fatiando uma lista
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:]) #Apresenta os 3 ultimos jogadores da lista

#Copiando uma lista
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]      #sem [:] ele n copia a lista ele atribui friend_foods a lista
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

#Criando tupla (lista imutavel)
dimensions = (200, 50)
print("Original dimensions:")
print(dimensions[0])
print(dimensions[1])

#Sobrescrevendo uma tupla
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

#Testando varias condiçoes
age_0 = 22
age_1 = 18
age_0 >= 21 or age_1 >= 21

#Verificando se um valor esta na lista
requested_toppings = ['mushrooms', 'onions', 'pineapple']
'mushrooms' in requested_toppings

#Verificando se uma lista nao esta vazia
requested_toppings = []

if requested_toppings:
    print("Nao esta vazia")
else:
    print("Are you sure you want a plain pizza?")