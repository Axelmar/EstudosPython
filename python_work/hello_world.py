
# Criando lista
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

#Adicionando elemento no final da lista
motorcycles.append('ducati')
print(motorcycles)

#Adicionando elemento em qualquer posição da lista
motorcycles.insert(4, 'bmw')
print(motorcycles)

#Removendo o ultimo elemento e guardando seu valor
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

#Removendo qualquer elemento e guardando seu valor
first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a ' + first_owned.title() + '.')

#Removendo elemento pelo seu valor
motorcycles.remove('ducati')
print(motorcycles)

#Ordenando a lista
motorcycles.sort()
print(motorcycles)

#Ordenando a lista temporariamente
cars = ['bmw', 'audi', 'toyota', 'subaru']

print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)