# Função com passagem de parametro
def greet_user(username):
    """Exibe uma saudação simples."""
    print("Hello, " + username.title() + "!")

greet_user('jesse')


# Funçao com argumentos posicionais
def describe_pet(animal_type, pet_name):
    """Exibe informaçoes sobre um animal de estimação."""
    print("\nI have a " + animal_type + '.')
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry')

# Funcao com argumento nomeado
describe_pet(animal_type='hamster',pet_name='harry')

# Funcao com valores default
def describe_pet2(pet_name, animal_type='dog'):
    print("\nI have a " + animal_type + '.')
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet2(pet_name='willie')

# Modificando uma lista em uma funçao
def print_models(unprinted_designs, completed_models):      # Usar [:] para enviar uma copia da lista para a funcao. Ex: nome_da_funcao(nome_da_lista[:])
    """
    Simula a impressao de cada design, até que nao haja mais nenhum.
    Transfere cada design para completed_models apos a impressao.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        #Simula a criação de uma impressao 3D a partir do design
        print("Printing model: " + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Mostra todos os modelos impressos."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# Passando um numero arbitrario de argumentos
def make_pizza(*toppings):
    """Exibe a lista de ingredientes pedidos."""
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# Usando argumentos nomeados arbitrarios
def build_profile(first, last, **user_info):
    """Constroi um dicionario contendo tudo que sabeos sobre um usuario."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)

# Modulaçao
def make_pizza_w_size(size, *toppings):
    """Apresenta a pizza que estamos prestes a preparar."""
    print("\nMaking a " + str(size) +
        "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)