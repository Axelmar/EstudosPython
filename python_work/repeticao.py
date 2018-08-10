#Percorrendo uma lista inteira com laço
magicians = ['alice', 'david', 'carolina']
for magician in magicians:          #Extrair um nome da lista magicians e armazena-lo na variavel magician
    print(magician.title() + ', that was a great trick!')
    print("I can't wait to see your next trick, " + magician.title() + ".\n")
print("Thank you, everyone. That was a great magic show!")

#Usando a funçao range()
for value in range(1,6):
    print(value)

#Criando lista com a funçao range
numbers = list(range(1,6))
print(numbers)

#Listando os numeros pares de 1 a 10
even_numbers = list(range(2,11,2))
print(even_numbers)

#Lista dos quadrados perfeitos de 1 a 10
squares = []
for value in range(1, 11):
    square = value**2
    squares.append(square)
print(squares)

#Idem ao anterior utilizando list comprehension (abrangencia de lista)
squares = [value**2 for value in range(1, 11)]
print(squares)